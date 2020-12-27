import string

chars = string.ascii_lowercase + 'abc'
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

nlist = []

for c in message:
	
	if c in chars:
		idx = chars.index(c)
		nlist.append(chars[idx+2])
	else:
		nlist.append(c)
print(''.join(nlist))

string.maketrans