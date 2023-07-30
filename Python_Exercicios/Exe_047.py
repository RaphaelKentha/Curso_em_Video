# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('Todos os numeros pares de 0 a 50:')
for aux in range(2, 52, 2):
    print(aux, end=' ') # end=' ' para não quebrar a linha

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mNumeros pares entre 1 e 50\33[m')) # centraliza o texto
print('=#' * 35)
print('Os numeros pares entre 1 e 50 são:')
print('Processando ...')
sleep(2)
for aux in range(1, 51):
    if aux % 2 == 0:
        print(aux)
print('\033[1;30;41m}#{|\033[m' * 20)
# falta otimizar esse codigo
'''