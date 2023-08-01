# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random

jogada_pc = random.randint(0, 10)
valaidacao_jogo = False
count_jogadas =0

while valaidacao_jogo == False:
    jogada_user = int(input('Digite um número entre 0 e 10: '))
    count_jogadas += 1
    if jogada_user == jogada_pc:
        valaidacao_jogo = True
    else:
        print('Você errou, tente novamente!')
print('Você acertou na {}ª tentativa'.format(count_jogadas))

# observe  que ao deixar 'jogada_pc' fora do loop, o programa não gera um novo número a cada tentativa
# meu codigo:
'''
from time import sleep
import random
validacao_jogo = False
contadao_de_tentativas = 0
while validacao_jogo == False:
    numero_aletorio_pc = random.randint(0, 10)
    numero_do_jogador = int(input('Digite um numero de 0 a 10: '))
    if numero_do_jogador == numero_aletorio_pc:
        validacao_jogo = True
        print('Computador pensando...')
        sleep(0.5)
        print('Você acertou!')
        print('O numero que o computador escolheu foi {}'.format(numero_aletorio_pc))
        print('O numero que você escolheu foi {}'.format(numero_do_jogador))
    else:
        print('Computador pensando...')
        sleep(0.5)
        print('Você errou!')
        print('O numero que o computador escolheu foi {}'.format(numero_aletorio_pc))
        print('O numero que você escolheu foi {}'.format(numero_do_jogador))
    contadao_de_tentativas += 1
print('Você precisou de {} tentativas para acertar!'.format(contadao_de_tentativas))
print('\033[1;30;41m}#{|\033[m' * 20)
'''
