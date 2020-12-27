#!/usr/bin/env python3
import random
import math
from getpass import getpass
import subprocess
import turtle


subprocess.run('clear', shell=True)
subprocess.run('figlet -f Bloody "P A T H U" | lolcat -a -d 1', shell=True)

username = input("Enter Username: ")
password = getpass("Enter Password: ")

###########################################################################################
####################                    GAMES              ################################
###########################################################################################

def turtle_game():
    wn = turtle.Screen()
    wn.bgpic('/home/taj/CODES/python/completed/fathima/avengers.gif')
    wn.title("Fathima Hifza")

    lin1 = turtle.Turtle()
    lin1.color('yellow')
    lin1.speed(0)
    lin1.hideturtle()
    lin1.penup()
    lin1.goto(-200, 210)
    lin1.pendown()
    lin1.forward(400)
    lin1.penup()
    lin1.goto(-200, -210)
    lin1.pendown()
    lin1.forward(400)

    a = turtle.Turtle()
    a.shape('turtle')
    a.color('red')
    a.speed(1)

    b = turtle.Turtle()
    b.shape('turtle')
    b.color('blue')
    b.speed(1)

    c = turtle.Turtle()
    c.shape('turtle')
    c.color('green')
    c.speed(1)


    a.up()
    a.goto(-150, -210)
    b.up()
    b.goto(0, -210)
    c.up()
    c.goto(150, -210)
    a.left(90)
    b.left(90)
    c.left(90)


    for i in range(500):
        if a.position()[1] >= 210.00 or b.position()[1] >= 210.00 or c.position()[1] >= 210.00:
            break
        adist = random.randint(0,10)
        bdist = random.randint(0,10)
        cdist = random.randint(0,10)
        a.forward(adist)
        b.forward(bdist)
        c.forward(cdist)


        if a.position()[1] >= 210:
            print("\033[36mRED wins!\033[0;0m")
            wn.clear()
            wn.bye()
            return 'red'

        elif b.position()[1] >= 210:
            print("\033[36mBlue wins!\033[0;0m")
            wn.clear()
            wn.bye()
            return 'blue'

        elif c.position()[1] >= 210:
            print("\033[36mGreen wins!\033[0;0m")
            wn.clear()
            wn.bye()
            return 'green'


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
		if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
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
			subprocess.run('espeak "rupees five has been added to your account"', capture_output=True, shell=True)
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




###########################################################################################
####################                  CODE                 ################################
###########################################################################################



def main():
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
					subprocess.run('clear', shell=True)
					print("------------------------")
					print("   Select Game Choice   ")
					print("------------------------\n1. RPS \n2. TURTLE RACE\n")
					opinion = input()
					

					if opinion == '1':
						subprocess.run('clear', shell=True)
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
					

					elif opinion == '2':
						subprocess.run('clear', shell=True)
						print("###############################################################################")
						print("\033[36m                              TURTLE-RACE \033[0m")
						print("###############################################################################")
						print("                                                                               ")
						input_option = input("Your Choice: ")
						game_result = turtle_game()
						if game_result == input_option.lower():
							print("---------------------------------")
							print("\033[1;32m      YOU WERE RIGHT!! \033[0;0m ")
							print("---------------------------------\n")
							print("Added Rs 50 to your account!")
							subprocess.run('espeak "rupees fifty has been added to your account"', capture_output=True, shell=True)
							with open('/home/taj/CODES/python/completed/fathima/balance.txt','r') as balancefile:
								balancef = balancefile.readlines()
								balist = [int(i) for i in balancef]
								balance = balist[0]
								balance += 50
								with open('/home/taj/CODES/python/completed/fathima/balance.txt','w') as writefile:
									writefile.write(str(balance))
						else:
							print("\033[1;31m---------------------------------")
							print("          YOU WERE WRONG!")
							print("---------------------------------\033[0;0m\n")


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



if __name__ == '__main__':
	try:
		main()


	except turtle.Terminator:
		stuff = input("\nDo you really want to quit?[Y/n]").lower()
		if stuff == 'y':
			quit()
		else:
			print("Something Went WRONG!!!")