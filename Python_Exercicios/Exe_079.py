# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_de_valores = []

while True:
    numeros = (int(input('Digite um valor: ')))
    if numeros not in lista_de_valores:
        lista_de_valores.append(numeros)
        print('Valor adicionado com sucesso!')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0] # [0] pega a primeira letra, strip() tira os espaços
        if continuar in 'N':
            break
    else:
        print('Valor duplicado! Não vou adicionar...')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'N':
            break
lista_de_valores.sort()
print(f'Você digitou os valores {lista_de_valores}')
print(f'O maior valor digitado foi {max(lista_de_valores)} nas posições ', end='')
print(f'{lista_de_valores.index(max(lista_de_valores)) + 1}°') # mostra a posição do maior valor
print(f'O menor valor digitado foi {min(lista_de_valores)} nas posições ', end='')
print(f'{lista_de_valores.index(min(lista_de_valores)) + 1}°') # mostra a posição do menor valor

# meu codigo:
'''
print('-='*35)
print('{:=^81}'.format('\33[30;42mValores únicos em lista\33[m'))
print('-='*35)

from time import sleep

lista_valores_unicos = []

while True:
    numeros_para_adicionar = int(input('Digite um número: '))
    if numeros_para_adicionar not in lista_valores_unicos:
        lista_valores_unicos.append(numeros_para_adicionar)
        sleep(0.33)
        print('Valor adicionado com sucesso!')
        if input('Deseja continuar? [S/N] ').upper() == 'N':
            break
    else:
        sleep(0.33)
        print('Valor duplicado! Não vou adicionar...')
        if input('Deseja continuar? [S/N] ').upper() == 'N':
            break
print(f'Os valores digitados foram: ', end='')
print(sorted(lista_valores_unicos))
print('\033[1;30;41m}#{|\033[m' * 20)
'''	