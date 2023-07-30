# Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500
soma_aux = 0
cont_3 = 0
for aux in range(3, 500, 3): # 3 porque 3 é o primeiro multiplo de 3
    if aux % 2 != 0:
        print(aux, end=' ')
        cont_3 += 1
        soma_aux += aux
print('\nA soma de todos os multiplos de 3 é: {}'.format(soma_aux))
print('\nA soma de todos os multiplos de 3 é: {}'.format(soma_aux))

# meu codigo:
# fiz usando listas
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mSoma entre todos os números ímpares que são múltiplos de três\33[m')) # centraliza o texto
print('=#' * 35)
print('Os numeros impares entre 1 e 500 são:')
print('Processando ...')
sleep(2)
somatorio_mult3 = []
for aux in range(0, 501, 3): # o ultimo numero não é contado, e esta com um passo de 3
    if aux % 2 != 0: # se o numero for impar, pois o resto da divisão por 2 é diferente de 0
        somatorio_mult3.append(aux) # adiciona o valor na lista
print('Esses numeros são multiplos de 3 e impares: {}'.format(somatorio_mult3))
print('O somatorio de todos os valores foi {}'.format(sum(somatorio_mult3)))
print('O numero de elementos na lista é {}'.format(len(somatorio_mult3))
print('\033[1;30;41m}#{|\033[m' * 20)
'''	
