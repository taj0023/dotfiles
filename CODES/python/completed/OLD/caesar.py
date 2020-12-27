#!/usr/bin/env python3
from string import ascii_lowercase
import sys

chars = ascii_lowercase + ascii_lowercase

if len(sys.argv) == 1:
	print('Usage: caesar "sentence"')
else:
	word = sys.argv[1]

	for i in range(1,27):
		og = ""
		for c in word:
			if c == " ":
				og += " "
			if c in ascii_lowercase:
				new_letter = chars[chars.index(c)+i]
				og += new_letter
		print(f"[+{str(i).zfill(2)}] \033[92m".rjust(5, " ")+og+"\033[0m")