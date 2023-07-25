# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
if numero1 > numero2:
    print('O primeiro valor é maior.')
elif numero2 > numero1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mComparador de Números\33[m')
print('=$'*40)
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
print('Aguarde...')
sleep(1)
if numero1 > numero2:
    print('O primeiro número é maior que o segundo.')
elif numero1 < numero2:
    print('O segundo número é maior que o primeiro.')
else:
    print('Os dois números são iguais.')
print('=$'*40)
'''