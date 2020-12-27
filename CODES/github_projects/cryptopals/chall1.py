#!/usr/bin/env python3
import base64
from binascii import unhexlify

# string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# hex_bytes = unhexlify(string)
# new = str(hex_bytes)
# print(new)
# bencoded = base64.b64encode(hex_bytes).decode()

# if bencoded == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t':
# 	print("Done")

thenga = hex.frombytes(base64.b64decode('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'))

if thenga == '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d':
	print("UNDAPPRI")