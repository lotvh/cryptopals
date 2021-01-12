#!/usr/bin/env python3
from XOR_cipher import *

def detect_XORed_string(candidate_strings):
    """ detects which string was XORed against in array of strings, returns the key
    and encrypted message """
    max_score = 0
    key_max_score = 0
    message_max_score = ""
    for string in candidate_strings:
        key, score = find_key(string)
        if score > max_score:
            max_score = score
            key_max_score = key
            message_max_score = XOR_bytes_single(string, key_max_score)
    return key_max_score, message_max_score

if __name__ == "__main__":
    ciphertexts = [bytes.fromhex(string.strip()) for string in open("4.txt")]

    key, message_bytes = detect_XORed_string(ciphertexts)

    # nicely print resulting message
    print("Message: {}, key: {}".format(message_bytes.decode().rstrip(),
                                        chr(key)))

