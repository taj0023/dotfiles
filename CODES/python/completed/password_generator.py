#!/usr/bin/env python3
import random
import string
from itertools import cycle
import json
import sys
import os
from time import sleep
from getpass import getpass
import pyperclip

def decrypt():
	decrypted = "".join([chr(ord(a) ^ ord(b)) for a, b in zip(open('passwords.json', 'rb').read().decode(), cycle(master))])
	return decrypted.replace("'", "\"")


def encrypt(js):
	return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(str(js), cycle(master))])

def setup():
	print("Pushing master password to the database.")
	for i in range(5):
		print("Setting up everything" + i * ' . ')
		print("\033[A\033[A")
		sleep(0.5)
	print("Master password set successfully...!")
	print("Login again for the program to take effect.")
	print("Commands: clear, display")

if 'passwords.json' not in os.listdir('.'):
	master = getpass("Setup your new master password: ")
	setup()
	key_stuff = encrypt('[{"key": "unda"}]')
	with open('passwords.json', 'w') as new_file:
		new_file.write(key_stuff)
	sys.exit()
else:
	master = getpass("Enter the master password : ")


def clear():
	with open('passwords.json', 'w') as f:
		moisage = encrypt('[{"key": "unda"}]')
		f.write(moisage)
		print("Successfully cleared all data!")

def generate():
	platform = input("Enter the platform name   : ")
	ui = int(input('Enter the length of pass  : '))

	fol = ui // 2 + 1 if ui % 2 != 0 else ui // 2
	lol = ui // 2 - 1 if ui % 2 != 0 else ui // 2

	first = random.sample(list((string.ascii_lowercase + string.ascii_uppercase) * 2), fol)
	mid = list(random.choice(list('!@#$&')))
	last = random.sample(list(string.digits * 5), lol)

	passwd = "".join(first + mid + last)
	return passwd, platform

def display():
	di = json.loads(decrypt())[1:]
	if len(di) == 0:
		print("No records Found!")
		return
	print("==================================================")
	for i in di:
		for k,v in i.items():
			print(f"{k.ljust(15)} : {v}")
		print("==================================================")	

def main():

	passwd, platform = generate()
	print(f"generated password: \033[30;40m{passwd}\033[0m      (invisible! highlight to see. Copied to clipboard! ✅)")
	pyperclip.copy(passwd)
	data = {
		"platform_name": platform,
		"password": passwd
	}

	decoded = json.loads(decrypt())
	decoded.append(data)
	encoded = encrypt(decoded)
	with open('passwords.json', 'w') as fi:
		fi.write(str(encoded))


if __name__ == '__main__':
	if 'key' not in decrypt():
		print("Wrong Master Password!")
		sys.exit()
	if 'display' in sys.argv:
		display()
		sys.exit()
	elif 'clear' in sys.argv:
		clear()
		sys.exit()
	main()
