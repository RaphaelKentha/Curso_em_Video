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
