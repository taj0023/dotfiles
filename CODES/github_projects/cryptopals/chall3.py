from binascii import unhexlify

# hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
byte_string = unhexlify(hex_string)

for key in range(256):
    res = ""
    for b in byte_string:
        res += chr(b ^ key)
    
    try:
        thenga = str(res.encode('ascii'))
        if '\\' not in thenga:   
            print(thenga, key)
    except UnicodeEncodeError:
        pass


#'key' is 88. i.e, 'X'