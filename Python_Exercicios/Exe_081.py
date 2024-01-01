# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_numeros = []

while True:
    lista_numeros.append(int(input('Digite um número: ')))
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
print(f'Foram digitados {len(lista_numeros)} números')
print(f'Os números digitados foram: {sorted(lista_numeros, reverse=True)}') # mostra a lista em ordem decrescente
if 5 in lista_numeros:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')

# meu codigo:
'''
print('-='*35)
print('{:=^81}'.format('\33[30;42mLista ordenada\33[m'))
print('-='*35)

from time import sleep

lista_varios_valores = []
count_varios_valores = 0

while True:
    lista_varios_valores.append(int(input('Digite um número: ')))
    sleep(0.23)
    count_varios_valores += 1
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
print(f'Foram digitados {count_varios_valores} números')
print(f'Os números digitados foram: {sorted(lista_varios_valores, reverse=True)}') # mostra a lista em ordem decrescente
if 5 in lista_varios_valores:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')
print('\033[1;30;41m}#{|\033[m' * 20)
'''