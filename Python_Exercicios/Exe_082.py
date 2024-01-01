# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

import math

lista_par_impar = []
lista_par = []
lista_impar = []

while True:
    lista_par_impar.append(int(input('Digite um número: ')))
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
print(f'A lista completa é: {sorted(lista_par_impar)}')
for aux in lista_par_impar:
    if math.fmod(aux, 2) == 0:
        lista_par.append(aux)
    else:
        lista_impar.append(aux)
print(f'A lista de pares é: {sorted(lista_par)}')
print(f'A lista de ímpares é: {sorted(lista_impar)}')

# meu codigo:
'''
print('-='*35)
print('{:=^81}'.format('\33[30;42mLista pares e ímpares\33[m'))
print('-='*35)

from time import sleep

lista_par_impar = []
lista_par = []
lista_impar = []

while True:
    lista_par_impar.append(int(input('Digite um número: ')))
    sleep(0.23)
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
for aux in lista_par_impar:
    if aux % 2 == 0:
        lista_par.append(aux)
    else:
        lista_impar.append(aux)
print(f'A lista completa é: {sorted(lista_par_impar)}')
print(f'A lista de pares é: {sorted(lista_par)}')
print(f'A lista de ímpares é: {sorted(lista_impar)}')
print('\033[1;30;41m}#{|\033[m' * 20)
'''	