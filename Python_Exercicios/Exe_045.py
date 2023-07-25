# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep
print('Escolha uma opção:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
opcao = int(input('Escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('Aguarde...')
sleep(1)
jogador = opcao
computador = randint(1, 3)

if jogador == 1:
    if computador == 1:
        print('Você escolheu Pedra e o computador também. Deu empate!')
    elif computador == 2:
        print('Você escolheu Pedra e o computador escolheu Papel. Você perdeu!')
    elif computador == 3:
        print('Você escolheu Pedra e o computador escolheu Tesoura. Você ganhou!')
elif jogador == 2:
    if computador == 1:
        print('Você escolheu Papel e o computador escolheu Pedra. Você ganhou!')
    elif computador == 2:
        print('Você escolheu Papel e o computador também. Deu empate!')
    elif computador == 3:
        print('Você escolheu Papel e o computador escolheu Tesoura. Você perdeu!')
elif jogador == 3:
    if computador == 1:
        print('Você escolheu Tesoura e o computador escolheu Pedra. Você perdeu!')
    elif computador == 2:
        print('Você escolheu Tesoura e o computador escolheu Papel. Você ganhou!')
    elif computador == 3:
        print('Você escolheu Tesoura e o computador também. Deu empate!')
else:
    print('Opção inválida. Tente novamente.')

# meu codigo:
'''
from time import sleep
import random

print('=$'*40)
print('\t\t\t\33[30;42mJokenpô\33[m')
print('=$'*40)
print('Vamos jogar Jokenpô?')
print('Escolha uma das opções abaixo: ')
print('1 - Pedra\n2 - Papel\n3 - Tesoura')
pedra = 1
papel = 2
tesoura = 3
lista = [pedra, papel, tesoura]
jogada_do_computador = random.choice(lista)
jogada_do_jogador = int(input('Digite sua jogada: '))
print('Jon...')
sleep(1)
print('Ken...')
sleep(1)
print('Pô!!!')
sleep(1)
if jogada_do_computador == 1:
    print('O computador escolheu Pedra!')
elif jogada_do_computador == 2:
    print('O computador escolheu Papel!')
else:
    print('O computador escolheu Tesoura!')

if jogada_do_jogador == 1:
    print('Você escolheu Pedra!')
elif jogada_do_jogador == 2:
    print('Você escolheu Papel!')
else:
    print('Você escolheu Tesoura!')

if jogada_do_computador == jogada_do_jogador:
    print('Empate!')
elif jogada_do_computador == 1 and jogada_do_jogador == 2:
    print('Você ganhou!')
elif jogada_do_computador == 1 and jogada_do_jogador == 3:
    print('Você perdeu!')
elif jogada_do_computador == 2 and jogada_do_jogador == 1:
    print('Você perdeu!')
elif jogada_do_computador == 2 and jogada_do_jogador == 3:
    print('Você ganhou!')
elif jogada_do_computador == 3 and jogada_do_jogador == 1:
    print('Você ganhou!')
elif jogada_do_computador == 3 and jogada_do_jogador == 2:
    print('Você perdeu!')
else:
    print('Jogada inválida!')
print('=$'*40)
'''