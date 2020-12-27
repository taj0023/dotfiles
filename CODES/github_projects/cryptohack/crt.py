#!/usr/bin/env python3
from Crypto.Util.number import inverse

a1, a2, a3 = 2, 3, 5
n1, n2, n3 = 5, 11, 17

N1, N2, N3 = n2*n3, n3*n1, n1*n2
x1, x2, x3 = inverse(N1, n1), inverse(N2, n2), inverse(N3, n3)

x = a1*N1*x1 + a2*N2*x2 + a3*N3*x3

print(x % (5*11*17))