#!/usr/bin/env python3

input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"

def byte_xor(string1, string2):
    """ XOR two byte strings """
    return bytes([_string1 ^ _string2 for _string1, _string2 in zip(string1, string2)])

# find XOR combination of strings
XOR_bytes = byte_xor(bytes.fromhex(input1), bytes.fromhex(input2))

# Alternative, without using raw bytes (not recommended):
# first interpret hex strings as base-16 integers, XOR them and convert back
XOR_hex = hex(int(input1, 16) ^ int(input2, 16))

print(XOR_bytes.hex())
