# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

count_while = 0
soma_numero = 0
maior_numero = 0
menor_numero = 0

while True:
    numero = int(input('Digite um número: '))
    parada = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    count_while += 1
    soma_numero += numero
    if parada == 'N':
        break
    else:
        if count_while == 1:
            maior_numero = numero
            menor_numero = numero
        else:
            if numero > maior_numero:
                maior_numero = numero
            elif numero < menor_numero:
                menor_numero = numero
print('A média dos números digitados é {}'.format(soma_numero / count_while))
print('O maior número digitado foi {}'.format(maior_numero))
print('O menor número digitado foi {}'.format(menor_numero))

# meu codigo usando listas:
'''
from time import sleep
from statistics import median

print('#=' * 35)
print('{:=^81}'.format('\33[30;42mMédia, maior e menor valor\33[m'))
print('#=' * 35)

lista_numeros65 = []
aux65 = False
while aux65 == False:
    lista_numeros65.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        aux65 = True
print('Aguarde...')
sleep(1)
print('A quantidade de numeros digitados foi {}'.format(len(lista_numeros65)))
print('Os numeros digitados foram {}'.format(lista_numeros65))
print('A mediana dos numeros digitados é {}'.format(median(lista_numeros65))) # mediana
print('A mediana dos numeros digitados é {}'.format(sorted(lista_numeros65)[len(lista_numeros65) // 2])) # mediana
print('A média dos numeros digitados é {}'.format(sum(lista_numeros65) / len(lista_numeros65)))
print('O maior numero digitado foi {}'.format(max(lista_numeros65)))
print('O menor numero digitado foi {}'.format(min(lista_numeros65)))
print('\033[1;30;41m}#{|\033[m' * 20)
'''