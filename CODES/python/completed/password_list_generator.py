#!/usr/bin/env python3 

import itertools
from tqdm import tqdm
import sys


def questions():
	returning_list = []
	returning_list.append(input("Enter first name    : "))
	returning_list.append(input("Enter surname name  : "))
	returning_list.append(input("Enter last name     : "))
	returning_list.append(input("Enter Nick name     : "))
	returning_list.append(input("Enter DOB           : "))
	returning_list.append(input("Enter Lucky number? : "))
	returning_list.append(input("Enter gf/bf name    : "))
	for each in input("Enter other words   :").split(','):
		returning_list.append(each)
	return [p for p in returning_list if p]


def ask_length():
	ronge = input("Enter the range of length: ")
	mini, maxi = [int(i) for i in ronge.split()]
	return ronge, mini, maxi


def main():
	if '-i' in sys.argv:
		ls = questions()
		ronge, mini, maxi = ask_length()
	else:
		ls = input("Enter the words u want to be in dictionary:\n").split(',')
		ls = [i.strip() for i in ls]
		ronge, mini, maxi = ask_length()
	nlist = []
	for n in range(mini, maxi):
		noice = itertools.permutations(ls, n)
		for i in noice:
			nlist.append("".join(i))

	with open('./pass_list.txt', 'w') as pass_list:
		for i in tqdm(nlist):
			pass_list.write(i + '\n')


if __name__ == '__main__':
	main()
