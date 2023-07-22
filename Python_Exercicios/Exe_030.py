# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))

# Meu codigo abaixo:
'''
import math

leia_numero = int(input('Digite um numero inteiro: '))
if math.fmod(leia_numero, 2) == 0: # verifica se o resto da divisao e igual a zero
    print('O numero {} e par'.format(leia_numero))
else:
    print('O numero {} e impar'.format(leia_numero))
# usando o fmod, e possivel verificar se um numero e par ou impar
# pois o mesmo retorna o resto da divisao
print('Fim do programa')
print('#' * 50)

'''