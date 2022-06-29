file = ""
while True:
	a = input(" Type e to encrypt \n Type d to decrypt:\n- ")
	if a == "e":
		file = "encrypter"
	elif a == "d":
		file = "decrypter"
	elif a == "exit":
		break
	else:
		print("Sorry the program didn't understand that...")
	__import__(file)
