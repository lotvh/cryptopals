#!/usr/bin/env python3
import base64
import numpy as np
from itertools import combinations
from bitstring import BitArray
from XOR_cipher import find_key

def Hamming_distance(string1, string2):
    """ finds edit distance between two string on a binary level """
    #string2 = ' '.join(format(ord(x), 'b').zfill(8) for x in string2)
    string1 = BitArray(bytes=string1)
    string2 = BitArray(bytes=string2)
    assert len(string1.bin) == len(string2.bin)

    return sum(s1 != s2 for s1,s2 in zip(string1.bin,string2.bin))

def probable_keysize(data_bytes, number_blocks):
    """ finds 3 keysizes with lowest edit distance between a number of blocks
    of keysize length in ciphertext """
    av_distances = {}

    for keysize in range(2,41):

        blocks = [data_bytes[i : i + keysize]
                  for i in range(0, len(data_bytes), keysize)][:number_blocks]

        distances = [Hamming_distance(blocks[i], blocks[j])
                     for (i,j) in list(combinations(list(range(0,number_blocks)),2))]

        av_distances[keysize] = np.mean(distances) / keysize

    return sorted(av_distances, key=av_distances.get)[:3]

def break_repkey_XOR(data_bytes, keysizes):
    """ uses 3 most probable keysizes to divide up ciphertext into blocks of
    keysize length, then applies single character XOR decryption on strings
    of the nth character in each block, returns resulting keys for each block """
    keysize_keys = []

    for keysize in keysizes:
        blocks = []

        # divide ciphertext into blocks of length keysize, add padding to last
        # block to make it length keysize
        for i in range(0, len(data_bytes), keysize):
            block = data_bytes[i : i + keysize]
            block = block.ljust(keysize, b'\0')
            blocks.append(list(block))

        # convert type blocks from list into numpy array, transpose to get arrays
        # of nth character
        blocks = np.array(blocks)
        blocksT = blocks.transpose()

        # change type back to list in order to convert back to raw bytes
        blocksT = blocksT.tolist()
        blocksT = [bytes(blocksT[i]) for i in range(len(blocksT))]

        # do single character XOR decryption on each block and save keys
        block_keys = []
        for block in blocksT:
            key, score = find_key(block)
            block_keys.append(chr(key))
        keysize_keys.append(block_keys)

    return keysize_keys

if __name__ == "__main__":
    KEYSIZE = 0

    string1 = "this is a test"
    string2 = "wokka wokka!!!"

    assert Hamming_distance(bytes(string1, 'ascii'), bytes(string2, 'ascii')) == 37

    input_data = open("6.txt")
    data_bytes = base64.b64decode(input_data.read())

    keysizes = probable_keysize(data_bytes, 4)
    result = break_repkey_XOR(data_bytes, keysizes)
    print(''.join(result[0]))
