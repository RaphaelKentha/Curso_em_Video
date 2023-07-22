# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
import time
from time import sleep
ano = int(input('Digite um ano: '))
print('Analisando...')
sleep(3)
if ano == 0:
    ano = time.localtime().tm_year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
print('Fim do programa')

#meu codigo abaixo:
'''	
# Leia o ano corrente, e decubra se o mesmo e bissexto

ano_corrente = int(input('Digite o ano corrente: '))
if math.fmod(ano_corrente, 4) == 0 and math.fmod(ano_corrente, 100) != 0 or math.fmod(ano_corrente, 400) == 0:
    print('O ano {} e bissexto'.format(ano_corrente))
else:
    print('O ano {} nao e bissexto'.format(ano_corrente))

import calendar

if calendar.isleap(ano_corrente) == True:
    print('O ano {} e bissexto'.format(ano_corrente))
else:
    print('O ano {} nao e bissexto'.format(ano_corrente))
print('Fim do programa')
print('#' * 50)
'''