# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random

mao_pc = random.randint(0, 5)
count_vitorias = 0
print(mao_pc)
while True:
    mao_jogador = int(input('Digite um número de 0 a 5: '))
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if (mao_jogador + mao_pc) % 2 == 0 and parimpar == 'P':
        print('Você venceu!')
        count_vitorias += 1
    elif (mao_jogador + mao_pc) % 2 != 0 and parimpar == 'I':
        print('Você venceu!')
        count_vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'Você venceu {count_vitorias} vezes')

# meu codigo:
'''
from time import sleep
import random

print('-='*35)
print('{:=^81}'.format('\33[30;42mPar ou Impar\33[m'))
print('-='*35)

numero_vitorias = 0

while True:
    mao_jogador = int(input('Digite um número de 0 a 5: '))
    par_impar = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    mao_pc = random.randint(0, 5)
    print("PAR..")
    sleep(0.3)
    print("OU..")
    sleep(0.3)
    print("IMPAR..")
    sleep(0.3)
    if (mao_pc + mao_jogador) % 2 == 0 and par_impar == 'P':
        numero_vitorias += 1
        print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU PAR')
        print('Você VENCEU!')
    elif (mao_pc + mao_jogador) % 2 != 0 and par_impar == 'I':
        numero_vitorias += 1
        print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU IMPAR')
        print('Você VENCEU!')
    else:
        if par_impar == 'P':
            print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU IMPAR')
            print('Você PERDEU!')
        else:
            print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU PAR')
            print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {numero_vitorias} vezes.')
print('\033[1;30;41m}#{|\033[m' * 20)
'''