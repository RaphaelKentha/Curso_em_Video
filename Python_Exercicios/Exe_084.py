#desafio 084
# Faça um programa que leia nome e peso de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_pessoas = []
lista_pesos = []
count = 0

while True:
    lista_pessoas.append(str(input('Nome: ')))
    #adiciona o nome na lista
    lista_pesos.append(float(input('Peso: ')))
    #adiciona o peso na lista
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    count += 1
    if continuar == 'N':
        break
#como nao e "preciso" definir chave valor, usamos a lista de forma sequencial
print(f'Foram cadastradas {count} pessoas')
print(f'O maior peso foi de {max(lista_pesos)}Kg. Peso de ', end='')
#usa o max para encontrar o maior peso na lista de pesos
for aux in range(0, len(lista_pesos)):
    if lista_pesos[aux] == max(lista_pesos):
        print(f'{lista_pessoas[aux]} ', end='')
        #como o acesso e sequencial, podemos usar o indice do peso para acessar o nome correspondente
print(f'\nO menor peso foi de {min(lista_pesos)}Kg. Peso de ', end='')
#usa o min para encontrar o menor peso na lista de pesos
for aux in range(0, len(lista_pesos)):
    if lista_pesos[aux] == min(lista_pesos):
        print(f'{lista_pessoas[aux]} ', end='')
        #como o acesso e sequencial, podemos usar o indice do peso para acessar o nome correspondente
