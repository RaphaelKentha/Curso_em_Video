# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão
primeiro_termo_pa = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
for aux in range(1, 11):
    print(primeiro_termo_pa + (aux - 1) * razao_pa, end=' -> ')
print('FIM')

# meu codigo:
'''
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mProgressão aritmética\33[m'))
print('=#' * 35)
primeiro_termo_pa = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
print('Processando ...')
sleep(2)
for aux in range(primeiro_termo_pa, primeiro_termo_pa + (razao_pa * 10), razao_pa):
    print(aux)
print('\033[1;30;41m}#{|\033[m' * 20)
'''	