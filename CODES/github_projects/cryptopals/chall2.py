from Crypto.Util.number import bytes_to_long, long_to_bytes

h1 = '1c0111001f010100061a024b53535009181c'
h2 = '686974207468652062756c6c277320657965'

hb1, hb2 = bytes.fromhex(h1), bytes.fromhex(h2)
hbl1, hbl2 = bytes_to_long(hb1), bytes_to_long(hb2)
ans = hbl1 ^ hbl2

assert hex(ans)[2:] == '746865206b696420646f6e277420706c6179'
 