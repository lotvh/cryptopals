#!/usr/bin/env python3

def repXOR_encryption(string_bytes, key_bytes):
    """ encrypts a string in raw bytes using repeated XOR combination using a
    key of any length """
    encrypted_string = []
    iter = 0
    for _byte in string_bytes:
        encrypted_string+= bytes([_byte ^ key_bytes[iter]])
        iter = (iter+1)%len(key_bytes)
    return encrypted_string

def pretty_printing(encrypted_string):
    encrypted_string = [hex(encrypted_string[i])[2:].zfill(2) for i in range(0, len(encrypted_string))]
    print(''.join(encrypted_string))

if __name__ == "__main__":

    input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"

    encrypted_string = repXOR_encryption(bytes(input, 'utf-8'), bytes(key, 'utf-8'))
    pretty_printing(encrypted_string)
