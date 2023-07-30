# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o
soma_6 = 0
for aux in range(1,7):
    num = int(input('Digite o {}º numero: '.format(aux)))
    if num % 2 == 0:
        print('O numero {} é par'.format(num))
        soma_6 += num
print('A soma dos numeros pares é {}'.format(soma_6))

# meu codigo:
# fiz com lista
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mSoma dos numeros pares\33[m'))
print('=#' * 35)
somatorio_pares = []
print('Digite 6 numeros inteiros: ')
for aux in range(0, 6):
    valor_par = int(input('Digite o valor numero {}: '.format(aux + 1)))
    if valor_par % 2 == 0:
        somatorio_pares.append(valor_par) # adiciona o valor na lista
print('Processando ...')
sleep(2)
print('Os numeros pares digitados foram: {}'.format(somatorio_pares))
print('O somatorio dos numeros pares digitados foi: {}'.format(sum(somatorio_pares)))
print('\033[1;30;41m}#{|\033[m' * 20)
'''	