#desafio 100
# Faça um programa que tenha uma lista chamada números e
#  duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
#  dentro da lista e a segunda função vai mostrar a soma
#  entre todos os valores pares sorteados pela função anterior.

from random import randint

lista_numeros = list()

def sorteador():
    print('Sorteando 5 valores da lista: ', end='')
    for aux in range(5):
        lista_numeros.append(randint(1, 10))
        print(lista_numeros[aux], end=' ')

def soma_par():
    acumulador = 0
    for aux in lista_numeros:
        if aux % 2 == 0:
            acumulador += aux
    print(f'\nSomando os valores pares de {lista_numeros}, temos {acumulador}')

sorteador()
soma_par()