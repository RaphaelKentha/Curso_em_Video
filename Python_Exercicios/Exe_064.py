# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

aux_while = 0
count_while = 0

while aux_while != 999:
    aux_while = int(input('Digite um número: '))
    count_while += aux_while
    if aux_while == 999:
        break # break para sair do loop
    else:
        aux_while = int(input('Digite um número: '))
print('A soma dos números digitados é {}'.format(count_while))

# meu codigo:
'''
from time import sleep
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mSoma de números inteiros\33[m'))
print('#=' * 35)
cont_numero = 0
soma_numero = 0
valid_999 = False
while valid_999 == False:
    num_inteiro = int(input('Digite o {} numero: '.format(cont_numero + 1)))
    if num_inteiro == 999:
        valid_999 = True
    else:
        cont_numero += 1
        soma_numero += num_inteiro
print('Aguarde...')
sleep(1)
print('A soma dos {} numeros digitados é {}'.format(cont_numero, soma_numero))
print('\033[1;30;41m}#{|\033[m' * 20)
'''