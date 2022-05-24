#!/bin/bash python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "crypter.py" or file == "thekey.key" or file == "decrypter.py":
            continue
    if os.path.isfile(file):
            files.append(file)

print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()


secretphrase = "secret"

user_phrase = input("Enter secret passphrase to decrypt files\n")

if user_phrase == secretphrase:
    for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print("Files have been decrypted")
else:
        print ("Sorry, try again")