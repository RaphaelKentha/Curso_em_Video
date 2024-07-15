#desafio 88
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random


lista_jogos = []
lista_numeros = []
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))


for aux in range(1, quantidade_jogos + 1):
    for aux2 in range(1, 7):
        num = random.randint(1, 60)
        lista_numeros.append(num)
    lista_jogos.append(lista_numeros[:])
    lista_numeros.clear()

for aux in range(1, quantidade_jogos + 1):
    print(f'Jogo {aux}: {lista_jogos[aux - 1]}')
