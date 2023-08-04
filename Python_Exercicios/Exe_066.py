# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre elas (desconsiderando o flag)

count66 = 0
soma66 = 0

print('Digite 999 para parar o programa')
while True:
    num66 = int(input('Digite um número: '))
    if num66 == 999:
        break
    count66 += 1
    soma66 += num66
print(f'Você digitou {count66} números e a soma entre eles foi {soma66}')

# meu codigo:
'''
from time import sleep
print('-='*35)
print('{:=^81}'.format('\33[30;42mLer numero\33[m'))
print('-='*35)
print('Digite 999 para parar')
somo66 = 0
conta66 = 0
while True:
    numero66 = int(input('Digite um número: '))
    if numero66 == 999:
        break
    somo66 += numero66
    conta66 += 1
print('Finalizando...')
sleep(1)
print(f'A soma dos {conta66} números digitados é {somo66}')
print('\033[1;30;41m}#{|\033[m' * 20)
'''