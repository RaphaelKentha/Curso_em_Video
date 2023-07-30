# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('Contagem regressiva para o estouro de fogos de artifício:')
for aux in range(10, -1, -1):
    print(aux)
    sleep(1)
print('BUM! BUM! POOOW!')

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mContagem regressiva para o estouro de fogos de artifício\33[m')) # centraliza o texto
print('=#' * 35)
for aux in range(11, 0, -1):
    print("...{}".format(aux - 1)) # -1 para não mostrar o numero 11, e o 0 esta fora do range
    sleep(1)
print('what ....???')
sleep(2)
print('BUM! BUM! POOOW!')
print('\033[1;30;41m}#{|\033[m' * 20)
'''