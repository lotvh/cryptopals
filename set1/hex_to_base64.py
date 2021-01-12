#!/usr/bin/env python3
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# convert to raw bytes
hex_in_bytes = bytes.fromhex(hex_string)

# encode raw bytes in base64
base64_bytes = base64.b64encode(hex_in_bytes)

print(hex_in_bytes)
print(base64_bytes)
