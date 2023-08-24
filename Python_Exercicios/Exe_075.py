# Desenvolva um programa que leia quatro valores pelo teclado e 
# guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

tupla_armazena4 = ()
conta9 = conta3 = conta_par = 0

while True:
    num = int(input('Digite um número: '))
    tupla_armazena4 += (num,)
    if num == 9:
        conta9 += 1
    if num == 3:
        conta3 += 1
    if num % 2 == 0:
        conta_par += 1
    if len(tupla_armazena4) == 4:
        break
print(f'Você digitou os valores {tupla_armazena4}')
print(f'O valor 9 apareceu {conta9} vezes')
while True:
    if conta3 > 0:
        print(f'O valor 3 apareceu na {tupla_armazena4.index(3)+1}ª posição')
        break
    else:
        print('O valor 3 não foi digitado')
        break
print(f'Os valores pares digitados foram: ', end = '')
for aux in range(0, len(tupla_armazena4)):
    if tupla_armazena4[aux] % 2 == 0:
        print(tupla_armazena4[aux], end = ' ')
        break
    else:
        print('Não foram digitados valores pares')
        break

# meu codigo:
'''
from time import sleep

print('-='*35)
print('{:=^81}'.format('\33[30;42mNúmeros aleatórios\33[m'))
print('-='*35)

tupla_de_4 = ()
conta_9 = 0
posicao_3 = 0

print('Digite 4 números')
for aux in range(0, 4):
    tupla_de_4 += (int(input('Digite um número: ')),) # a vírgula é necessária para que o programa entenda que é uma tupla
    sleep(0.1)
    if tupla_de_4[aux] == 9:
        conta_9 += 1
    elif tupla_de_4[aux] == 3:
        posicao_3 = aux + 1
    if tupla_de_4[aux] % 2 == 0: # se o resto da divisão por 2 for 0
        print(f'{tupla_de_4[aux]} é par')
print(f'O número 9 apareceu {conta_9} vezes')
if posicao_3 == 0:
    print('O número 3 não apareceu')
else:
    print(f'O número 3 apareceu na posição {posicao_3}')
print(f'Você digitou os valores {tupla_de_4}')
print('\033[1;30;41m}#{|\033[m' * 20)
'''