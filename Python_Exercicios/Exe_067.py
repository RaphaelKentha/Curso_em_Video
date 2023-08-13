# Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando o número 
# solicitado for negativo

while True:
    numero_tabuada = int(input('Digite um número para ver sua tabuada: '))
    if numero_tabuada < 0:
        print('Programa encerrado!')
        break
    else:
        for aux in range(1, 11):
            print(f'{numero_tabuada} x {aux} = {numero_tabuada * aux}')

# meu codigo:
'''
from time import sleep
print('-='*35)
print('{:=^81}'.format('\33[30;42mTabuada\33[m'))  
print('-='*35)

numero_tabuada = 0

while True:
    numero_tabuada = int(input('Digite um número para ver sua tabuada: '))
    if numero_tabuada < 0:
        break
    for aux in range(1, 11):
        print(f'{numero_tabuada} x {aux} = {numero_tabuada * aux}')
        sleep(0.3)
print('Finalizando...')
sleep(1)
print('\033[1;30;41m}#{|\033[m' * 20)
'''