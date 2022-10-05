#!/usr/bin/python3

print('Filskrivning exempel')

f = open('minSkrivFil.txt',mode='w')

f.write("En testrad\n")
f.write("En till rad\n")

f.close()

