#!/usr/bin/python3

#fråga användare om hund är hungrig
svar = input('Är hund hungrig?')

'''
skriv ut mata hunden om svar 'ja'. Skriv ut 'hunden mätt' om svar 'nej'
annars, skriv ut 'förstår ej svar'
'''
if svar.lower() == 'ja':
   print(f'Du svarade {svar} - mata hunden!')
elif svar.lower() == 'nej':
   print(f'Du svarade {svar} - hunden mätt!')
else:
   print('förstår ej svar!')

print('***slut på program***')


