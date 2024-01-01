# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_valores = []
lista_maiores = []
lista_menores = []

for aux in range(0, 6):
    lista_valores.append(int(input(f'Digite um valor para a posição {aux + 1}: ')))
print(f'Você digitou os valores {lista_valores}')

for aux in range(0, 6):
    if lista_valores[aux] == max(lista_valores):
        lista_maiores.append(aux)
    if lista_valores[aux] == min(lista_valores):
        lista_menores.append(aux)
if len(lista_maiores) > 1:
    print(f'O maior valor digitado foi {max(lista_valores)} nas posições {lista_maiores}')
else:
    print(f'O maior valor digitado foi {max(lista_valores)} na posiçao {lista_maiores}')
if len(lista_menores) > 1:
    print(f'O menor valor digitado foi {min(lista_valores)} nas posições {lista_menores}')
else:
    print(f'O menor valor digitado foi {min(lista_valores)} na posiçao {lista_menores}')

# meu codigo:
'''
print('-='*35)
print('{:=^81}'.format('\33[30;42mMaior e menor valor em lista\33[m'))
print('-='*35)

from time import sleep

lista_cinco_valores =[]

for aux in range(0, 5):
    lista_cinco_valores.append(int(input(f'Digite um valor para a posição {aux + 1}°: ')))
    print(f'Valor {lista_cinco_valores[(aux)]}° adicionado na posição {aux + 1}° com sucesso!')
    sleep(0.5)
print(f'Os seguintes valores foram digitados: {lista_cinco_valores} ', end='')
print(f'\nO maior valor digitado foi {max(lista_cinco_valores)} nas posições ', end='')
print(f'{lista_cinco_valores.index(max(lista_cinco_valores)) + 1}°') # mostra a posição do maior valor
print(f'O menor valor digitado foi {min(lista_cinco_valores)} nas posições ', end='')
print(f'{lista_cinco_valores.index(min(lista_cinco_valores)) + 1}°') # mostra a posição do menor valor
print('\033[1;30;41m}#{|\033[m' * 20)
'''