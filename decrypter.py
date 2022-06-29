#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
notouch = ["main.py", "decrypter.py", "encrypter.py", "thekey.key"]

for file in os.listdir():
		if file in notouch:
				continue
		if os.path.isfile(file):
			files.append(file)
print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read() 

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
