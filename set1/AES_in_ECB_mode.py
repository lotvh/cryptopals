#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES
#from Crypto.Util.Padding import unpad

if __name__ == "__main__":

    input_data = open("7.txt")
    data_bytes = base64.b64decode(input_data.read())

    key = "YELLOW SUBMARINE"
    decipher = AES.new(key, AES.MODE_ECB)
    msg = decipher.decrypt(data_bytes)
    print(msg.decode("utf-8"))
