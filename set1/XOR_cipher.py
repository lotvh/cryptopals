#!/usr/bin/env python3
import base64

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def XOR_bytes_single(string_bytes, char):
    return bytes([_a ^ char for _a in string_bytes])

def plaintext_score(string_bytes):
    """ calculates score for how close a string is to plaintext English using
    the frequency of letters """
    score = 0

    for byte in string_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0.0)

    return score

def find_key(ciphertext):
    """ loops over all 256 possible keys
    1 hex character represents 4 bits, so keys are comprised of 2 characters,
    16*16 gives 256 possible keys """
    maximal_value = 0
    key = 0
    for possible_key in range(256):
        decrypt_bytes = XOR_bytes_single(ciphertext, possible_key)
        single_score = plaintext_score(decrypt_bytes)
        if single_score > maximal_value:
            maximal_value = single_score
            key = possible_key
    return key, maximal_value

if __name__ == "__main__":

    # always work in raw bytes
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = bytes.fromhex(input)

    key, score = find_key(ciphertext)

    # nicely print result
    message_bytes = XOR_bytes_single(ciphertext, key)
    print("Message: {}, key: {}".format(message_bytes.decode().rstrip(),
                                        chr(key)))
