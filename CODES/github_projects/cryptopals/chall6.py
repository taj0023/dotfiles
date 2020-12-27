#!/usr/bin/env python3
from base64 import b64decode

def ham_size(a, b):
	zlist = list(zip(a, b))
	return sum([bin(ord(i)^ord(j)).count('1') for i,j in zlist])


with open('chall6.txt') as f:
	msg = b64decode(f.read())

nlist = []
for KEYSIZE in range(2, 40):
	SIZE = KEYSIZE
	NEXT_SIZE = KEYSIZE+1
	first, second = msg[:KEYSIZE], msg[:NEXT_SIZE]
	normalize = ham_size(str(first), str(second)) / KEYSIZE
	nlist.append((normalize, KEYSIZE))
probable_key_size = sorted(nlist, key=lambda x: x[0])[0][1]


for i in range(len(msg)):
	blocks = msg[i:i+probable_key_size]
	first_block = [i for i in blocks][p]

