# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
valor_tabuada = int(input('Digite um numero para ver sua tabuada: '))
for aux in range(0, 11):
    print('{} x {} = {}'.format(valor_tabuada, aux, valor_tabuada * aux))

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mTabuada\33[m')) # centraliza o texto
print('=#' * 35)
valor_tabuada = int(input('Digite o valor da tabuada: '))
print('Processando ...')
sleep(2)
for aux in range(0, 11):
    print('{} X {} = {}'.format(valor_tabuada, aux, valor_tabuada * aux))
print('\033[1;30;41m}#{|\033[m' * 20)
'''