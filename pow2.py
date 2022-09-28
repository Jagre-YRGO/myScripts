#!/usr/bin/python3

def calcPowOfTwo(exp):
   return 2**exp

for i in range(0,8):
   print(f'2^{i}={calcPowOfTwo(i)}')
