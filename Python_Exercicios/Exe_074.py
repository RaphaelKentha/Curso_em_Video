# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e 
# o maior valor que estão na tupla

import random

tupla_aleatorio5 = random.sample(range(0, 100), 5) # random.sample() retorna uma lista com 5 números aleatórios

print(f'Os números aleatórios gerados foram: {tuple(tupla_aleatorio5)}')
print(f'O maior número gerado foi {max(tupla_aleatorio5)}')
print(f'O menor número gerado foi {min(tupla_aleatorio5)}')

# meu codigo:
'''
from time import sleep
import random

print('-='*35)
print('{:=^81}'.format('\33[30;42mNúmeros aleatórios\33[m'))
print('-='*35)
sleep(0.3)

tupla_numeros_aleatorios = random.sample(range(0, 100), 5) # gera 5 números aleatórios entre 0 e 100
#ou pode ser:
#for aux in range(0, 5):
#    tupla_numeros_aleatorios[aux] = random.randint(0, 100)
sleep(0.1)
print(f'Os números sorteados foram: {tupla_numeros_aleatorios}')
sleep(0.1)
print(f'O maior número sorteado foi {max(tupla_numeros_aleatorios)}')
sleep(0.1)
print(f'O menor número sorteado foi {min(tupla_numeros_aleatorios)}')
print('\033[1;30;41m}#{|\033[m' * 20)
'''