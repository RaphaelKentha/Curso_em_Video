# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
cont_primo = 0
numero_primo = int(input('Digite um numero inteiro: '))
for aux in range(1, numero_primo + 1):
    if numero_primo % aux == 0:
        cont_primo += 1
if cont_primo == 2:
    print('O numero {} é primo'.format(numero_primo))

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mNumero primo\33[m'))
print('=#' * 35)
numero_primo = int(input('Digite um numero inteiro: '))
variavel_prima = 0
print('Agrupando ...')
sleep(1)
for aux in range(1, numero_primo + 1):
    if numero_primo % aux == 0:
        print('\33[30;42m{}\33[m'.format(aux), end=' ')# end=' ' para não quebrar a linha
        variavel_prima += 1
    else:
        print('\33[30;41m{}\33[m'.format(aux), end=' ')
print('\nVerificando ...')
sleep(2)
if variavel_prima % 2 == 0 and variavel_prima == 2:
    print('O numero {} é primo.'.format(numero_primo))
else:
    print('O numero {} não é primo.'.format(numero_primo))
print('\033[1;30;41m}#{|\033[m' * 20)
'''	