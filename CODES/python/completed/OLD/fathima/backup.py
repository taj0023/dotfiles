#!/usr/bin/env python3
import random
import math
from getpass import getpass
import subprocess


subprocess.run('clear', shell=True)
subprocess.run('figlet -f Bloody "P A T H U" | lolcat -a -d 1', shell=True)

username = input("Enter Username: ")
password = getpass("Enter Password: ")


def rps():
	def play():
		my_list = ['r','p','s']
		computer = random.choice(my_list)

		user =input("\033[1mEnter Choice:\033[0;0m")

		if user == computer:
			return (0,user,computer)

		if iswin(user,computer):
			return (1,user,computer)

		return (-1,user,computer)



	def iswin(player,opponent):
		if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 's'):
			return True
		return False


	def best_of(n):
		playerwins = 0
		computerwins = 0
		winsnecessary = math.ceil(n/2)
		

		while playerwins < winsnecessary and computerwins < winsnecessary:
			result, user, computer = play()
			if result == 0:
				print("Your Choice: {}.......... Computer Choice: {}....\033[1;37m......TIE\033[0;0m".format(user,computer))

			elif result == 1:
				playerwins += 1

				print("Your Choice: {}.......... Computer Choice: {}....\033[1;32m......WIN\033[0;0m".format(user,computer))
			else:
				computerwins += 1
				print("Your Choice: {}.......... Computer Choice: {}....\033[1;31m......LOSE\033[0;0m".format(user,computer))

		if playerwins > computerwins:
			print("---------------------------------")
			print("\033[1;32m            YOU WON!! \033[0;0m ")
			print("---------------------------------")
			print("Added Rs 5 to your account!")
			subprocess.run('play output.mp3', capture_output=True, shell=True)
			with open('/home/taj/CODES/python/completed/fathima/balance.txt','r') as balancefile:
				balancef = balancefile.readlines()
				balist = [int(i) for i in balancef]
				balance = balist[0]
				balance += 5
				with open('/home/taj/CODES/python/completed/fathima/balance.txt','w') as writefile:
					writefile.write(str(balance))
		else:
			print("\033[1;31m-------------------------------")
			print(" \033[1;31m           YOU LOSE!!          ")
			print("-------------------------------\033[0;0m")


	best_of(5)









flag = 1
while flag == 1:
	

	if username == 'fathima':
		if password == 'khadheeja':
			print("\033c",end = '')
			print("Welcome to your bank account!")
			print("-----------------------------")
			print("1. Show your Balance")
			print("2. Play Games to get money!")
			print("3. Buy a TV \n")
			option = input()
			if option == '1':
				with open('/home/taj/CODES/python/completed/fathima/balance.txt','r') as balancefile:
					balancef = balancefile.readlines()
					balist = [int(i) for i in balancef]
					balance = balist[0]
				print("Your balance is Rs.",balance)
				thenga = input("Do you want to do another transaction?[y/n]")
				if thenga == 'y':
					continue
				else:
					flag = 0
				
			elif option == '2':
				print("###############################################################################")
				print("\033[36m                                R-P-S \033[0m")
				print("###############################################################################")
				print("                                                                               ")
				rps()

				thenga = input("Do you want to do another transaction?[y/n]")
				if thenga == 'y':
					continue
				else:
					flag = 0
			else:
				print("-----------------------------------------")
				print("You Dont have enough money to buy a TV!!!")
				print("-----------------------------------------")
				thenga = input("Do you want to do another transaction?[y/n]")
				if thenga == 'y':
					continue
				else:
					flag = 0
		else:
			print("Invalid Password!!")
			break

	else:
		print("Invalid Username!!")
		break