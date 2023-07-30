# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior_peso = 0
menor_peso = 0
for aux in range(0, 5):
    pessoa_peso = float(input('Digite o peso da {}ª pessoa: '.format(aux + 1)))
    if aux == 0: # se for a primeira pessoa a ser lida o maior e menor peso é o dela
        maior_peso = pessoa_peso
        menor_peso = pessoa_peso
    else:
        if pessoa_peso > maior_peso: # se a pessoa lida for maior que a anterior, ela é o novo maior peso
            maior_peso = pessoa_peso
        if pessoa_peso < menor_peso: # se a pessoa lida for menor que a anterior, ela é o novo menor peso
            menor_peso = pessoa_peso
print('O maior peso lido foi {}Kg'.format(maior_peso))
print('O menor peso lido foi {}Kg'.format(menor_peso))

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mMaior e menor peso\33[m'))
print('=#' * 35)
lista_de_pesos = []
for aux in range(0, 5):
    peso = float(input('Digite o peso da pessoa {}: '.format(aux + 1)))
    lista_de_pesos.append(peso)
print('Processando ...')
sleep(2)
print('O maior peso foi: {}Kg'.format(max(lista_de_pesos)))
print('O menor peso foi: {}Kg'.format(min(lista_de_pesos)))
print ('\033[1;30;41m}#{|\033[m' * 20)
'''