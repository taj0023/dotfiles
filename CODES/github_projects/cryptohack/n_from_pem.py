from Crypto.PublicKey import RSA

key = RSA.importKey(open('thenga.pem').read())
print(key.n)