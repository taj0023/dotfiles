import random
from words import words
import string
from PyDictionary import PyDictionary
import time
from turtle import *

wn = Screen()
wn.bgcolor('lightblue')
wn.title('Hangman')

w = window_width()
h = window_height()

def land():
    line = Turtle()
    line.speed(0)
    line.color('green')
    line.penup()
    line.goto(-w/2, -h/2)
    line.down()
    line.begin_fill()
    line.forward(w)
    line.left(90)
    line.forward(h/3.5)
    line.left(90)
    line.forward(w)
    line.left(90)
    line.forward(h/3.5)
    line.end_fill()
def stand():
    l = Turtle()
    l.speed(0)
    l.pensize(10)
    l.color('black')
    l.penup()
    l.goto(100, -200)
    l.pendown()
    l.forward(120)
    l.left(180)
    l.forward(60)
    l.right(90)
    l.forward(400)
    l.left(90)
    l.forward(160)
    l.left(90)
    l.forward(50)
def head():
    s = Turtle()
    s.hideturtle()
    s.speed(0)
    s.color('black')
    s.pensize(8)
    s.penup()
    s.goto(0,150)
    s.pendown()
    s.left(180)
    s.circle(30)
    s.circle(30, 180)
    s.right(90)   
def body():
    b = Turtle()
    b.hideturtle()
    b.pensize(8)
    b.penup()
    b.goto(0,90)
    b.pendown()
    b.right(90)
    b.forward(90)
def right_hand():
    r = Turtle()
    r.hideturtle()
    r.color('black')
    r.pensize(8)
    r.penup()
    r.goto(0,55)
    r.pendown()
    r.left(145)
    r.forward(50)
def left_hand():
    lh = Turtle()
    lh.hideturtle()
    lh.color('black')
    lh.pensize(8)
    lh.penup()
    lh.goto(0,55)
    lh.pendown()
    lh.left(35)
    lh.forward(50)
def left_leg():
    ll = Turtle()
    ll.hideturtle()
    ll.pensize(8)
    ll.right(180-45)
    ll.forward(60)
def right_leg():
    rl = Turtle()
    rl.hideturtle()
    rl.pensize(8)
    rl.right(45)
    rl.forward(60)

def get_meaning(word):
	dictionary = PyDictionary()
	meaning = dictionary.meaning(word)
	if 'Noun' in meaning.keys():
		thenga = "Noun : " + meaning['Noun'][0]
	if 'Verb' in meaning.keys():
		thenga = "Verb : " + meaning['Verb'][0]
	if 'Adjective' in meaning.keys():
		thenga = "Adj  : " + meaning['Adjective'][0]
	if 'Adverb' in meaning.keys():
		thenga = "Advb : " + meaning['Adverb'][0]
	if len(meaning) == 0:
		thenga = "No meaning found for this word!"

	return "Meaning : \n" + thenga
def print_tries(tries):
	tries_remaining = 10 - tries
	if tries_remaining < 2:
		return "\033[91mTries remaining:" + str(tries_remaining) + "\033[0m"
	elif tries_remaining < 4:
		return "\033[93mTries remaining:" + str(tries_remaining) + "\033[0m"
	else:
		return "\033[92mTries remaining:" + str(tries_remaining) + "\033[0m"
def error_print():

	print("I told you to enter a SINGLE character!")

def parts(tries_remaining):
    if tries_remaining <= 8:
        head()
        if tries_remaining < 6:
            body()
            if tries_remaining < 5:
                right_hand()
                if tries_remaining < 4:
	                left_hand()
	                if tries_remaining < 2:
	                    left_leg()
                    


def main():
	
	land()
	stand()
	word = random.choice(words).upper()
	used_letters = []
	correct_guesses = '-'*len(word)
	tries = 0
	
	while tries < 20:
		tries_remaining = 10 - tries -1
		parts(tries_remaining)
		print('\033c')
		print(' '.join(correct_guesses))
		unda = "Used Letters: " + ' '.join(used_letters)
		print(unda.ljust(50, ' ') + print_tries(tries))
		user_letter = input("Guess a letter: ").upper()
		if user_letter == '':
			continue
		if len(user_letter) > 1:
			error_print()
			time.sleep(2)
			continue
		
		if user_letter not in used_letters:
			used_letters.append(user_letter)
			if user_letter in word:
				idx = word.index(user_letter)
				correct_guesses = correct_guesses[:idx] + user_letter + correct_guesses[idx + 1:]
				tries -= 1
			tries += 1
			

		elif user_letter in used_letters:
			print("Already Used!")

		else:
			print("Invalid Character!!")

		if tries_remaining == 0:
			if 10 - tries == 1:
				if ''.join(list(correct_guesses)) == word:
					print('\033c')
					print(' '.join(correct_guesses))
					unda = "Used Letters: " + ' '.join(used_letters)
					print(unda.ljust(50, ' ') + print_tries(9))
					print("\033[92m---------------------------------------------")
					print("  Close call!! You Found it: " + correct_guesses)
					print("---------------------------------------------\033[0m")
					mean = input("Do you want to know the meaning of "+word+"?[Y/n]")
					if mean == 'y' or mean == 'Y':
						print("\033[92m" + get_meaning(word))
						break
					else:
						break
					break
			used_letters.append(user_letter)
			if user_letter in word:
				idx = word.index(user_letter)
				correct_guesses = correct_guesses[:idx] + user_letter + correct_guesses[idx + 1:]
				tries -= 1
				continue
			print('\033c')
			print(' '.join(correct_guesses))
			unda = "Used Letters: " + ' '.join(used_letters)
			print(unda[:len(unda)-1].ljust(50, ' ') + "Tries remaining:" + str(10 - tries))
			right_leg()
			print("\033[91m-----------------------------------------")
			print("    HANGED!!. The word was " + word)
			print("-----------------------------------------\033[0m")
			mean = input("Do you want to know the meaning of "+word+"?[Y/n]")
			if mean == 'y' or mean == 'Y':
				print("\033[92m" + get_meaning(word))
				break
			else:
				break

		if ''.join(list(correct_guesses)) == word:
			print("\033[92m---------------------------------------------")
			print("       You Found it: " + correct_guesses)
			print("---------------------------------------------\033[0m")
			mean = input("Do you want to know the meaning of "+word+"?[Y/n]")
			if mean == 'y' or mean == 'Y':
				print("\033[92m" + get_meaning(word))
				break
			else:
				break
			break
	wn.exitonclick()

if __name__ == "__main__":
	try:
		main()
	except AttributeError:
		print("Check your Network Connection!")
	except KeyboardInterrupt:
		print("\nGoodBye!")