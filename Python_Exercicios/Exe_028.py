# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para 
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever 
# na tela se o usuário venceu ou perdeu

import random
from time import sleep # Importa a função sleep da biblioteca time,com ela é possível fazer o programa esperar um tempo determinado

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = random.randint(0,5) # Faz o computador "pensar" em um número entre 0 e 5
num_user = int(input('Em que número eu pensei? ')) # Pergunta ao usuário qual número ele acha que o computador pensou
print('PROCESSANDO...')
sleep(3) # Faz o programa esperar 3 segundos
if num_user == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num,num_user))
#gostei muito da solucao acima, mas eu fiz uma solucao diferente, que tambem funciona(embora menos elegante)

'''
#desafio 028
# Escreva um programa que faca o computador "pensar"
# em um numero inteiro no intervalo de [0 - 5]
# e paca para o usuario tentar descobrir qual foi o numero
# e o resultado devera ser exibido na tela
import random

numeros_sorteados = random.randint(0, 5) # sorteia um numero inteiro entre 0 e 5
numero_do_usuario = int(input('Digite um numero inteiro entre 0 e 5: '))
if numero_do_usuario == numeros_sorteados:
    print('Parabens, voce acertou')
else:
    print('Que pena, voce errou')
print('O numero sorteado foi: {}'.format(numeros_sorteados))
print('O numero digitado: {}'.format(numero_do_usuario))
print('Fim do programa')
print('#' * 50)
'''