# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:])) # [2:] fatiamento para eliminar os dois primeiros caracteres
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:])) # [2:] fatiamento para eliminar os dois primeiros caracteres
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:])) # [2:] fatiamento para eliminar os dois primeiros caracteres
else:
    print('Opção inválida. Tente novamente.')

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mConversor de Bases Numéricas\33[m')
print('=$'*40)
numero = int(input('Digite um número inteiro: '))
opcao_de_conversao = int(input('Escolha uma das opções abaixo: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha: '))
print('Aguarde...')
sleep(1)
if opcao_de_conversao == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao_de_conversao == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao_de_conversao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
print('=$'*40)
'''