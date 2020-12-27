#!/usr/bin/env python3
from binascii import unhexlify

byte_message = bytes('ZRZHW[1FjESfIf4tf=^}aISqQZdH'.encode())
for key in range(256):
	res = ""
	for b in byte_message:
		res += chr(key ^ b)

	if res.isascii() and res.isprintable():
		if  len([i for i,c in enumerate(res) if c == " "]) > 3:
			print(key, res)