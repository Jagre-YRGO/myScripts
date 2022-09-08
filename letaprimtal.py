#!/usr/bin/python3

#ange max tal att prova
numbersToTest = int(input('Hur många tal vill du undersöka?: '))

#yttre loop - prova samtliga tal upp till numbersToTest
for i in range(1,numbersToTest+1):
   #inre loop - prova om talet i är jämt delbart med något annat tal än '1' och 'i'
   #isf är det ej ett primtal
   provenNotPrime = False
   for k in range(2,i):
      if i % k == 0:
         print(f'{i}',end = ',')
         provenNotPrime = True
         break
   #om vi lämnat den inre loopen utan att sätt provenNotPrime = True så har vi funnit ett primtal
   if provenNotPrime == False:
      print(f'\n*** {i} är ett Primtal! ***')

print('slut på program')
