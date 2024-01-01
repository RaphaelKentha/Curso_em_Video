#aula 17; modulo 3; curso em video
# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python
# As listas são variáveis compostas que permitem armazenar vários valores em 
# uma mesma estrutura, acessíveis por chaves individuais

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
print(lanche[1])
print(lanche[3]) # mostra o elemento 3 da lista
print(lanche[-2]) # mostra o penultimo elemento da lista
print(lanche[1:3]) # mostra os elementos 1 e 2 da lista
print(lanche[2:]) # mostra os elementos a partir do elemento 2
lanche[3] = 'Sorvete' # altera o elemento 3 da lista
lanche.append('Cookie') # adiciona um elemento no final da lista
lanche.insert(1,'Pizza') # adiciona um elemento na posição 1 da lista
lanche.insert(0, 'Cachorro Quente') # adiciona um elemento na posição 0 da lista
del(lanche[3]) # apaga o elemento 3 da lista
lanche.pop(3) # apaga o elemento 3 da lista
lanche.remove('Pizza') # apaga o elemento 'Pizza' da lista
if 'Pizza' in lanche:
    lanche.remove('Pizza') # apaga o elemento 'Pizza' da lista
numeros = [2, 5, 9, 1]
numeros.sort() # coloca os elementos da lista em ordem crescente
numeros.sort(reverse=True) # coloca os elementos da lista em ordem decrescente
len(numeros) # mostra quantos elementos tem na lista
numeros.insert(2, 0) # adiciona o elemento 0 na posição 2 da lista
numeros.append(7) # adiciona o elemento 7 no final da lista
numeros.pop() # apaga o último elemento da lista
valores = list(range(4, 11)) # cria uma lista com os valores de 4 a 10
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # coloca os elementos da lista em ordem crescente
for valor in valores:
    print(f'{valor}...', end='')
for index, valor in enumerate(valores):
    print(f'Na posição {index} encontrei o valor {valor}!')
numeros_A = list(range(0, 9)) # cria uma lista com os valores de 0 a 8
numeros_B = numeros_A[:] # cria uma cópia da lista numeros_A
numeros_B.insert(0, 11) # adiciona o elemento 11 na posição 0 da lista
print(numeros_A)
print(numeros_B)

#desafio 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas 
# respectivas posições na lista
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

#desafio 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente
print('-='*35)
print('{:=^81}'.format('\33[30;42mValores únicos em lista\33[m'))
print('-='*35)

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

#desafio 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista
# Já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela
print('-='*35)
print('{:=^81}'.format('\33[30;42mLista ordenada sem sort()\33[m'))
print('-='*35)

lista_pre_ordenada = []

for aux in range(0, 5):
    numero_adicionar = int(input('Digite um número: '))
    if len(lista_pre_ordenada) == 0:
        lista_pre_ordenada.append(numero_adicionar)
    else:
        for contador in range(0, len(lista_pre_ordenada)):
            if numero_adicionar <= lista_pre_ordenada[contador]:
                lista_pre_ordenada.insert(contador, numero_adicionar)
                break
            elif numero_adicionar > lista_pre_ordenada[-1]:
                lista_pre_ordenada.append(numero_adicionar)
                break
print(f'Os valores digitados foram: {lista_pre_ordenada}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 81
# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista
print('-='*35)
print('{:=^81}'.format('\33[30;42mLista ordenada\33[m'))
print('-='*35)

lista_varios_valores = []
count_varios_valores = 0

while True:
    lista_varios_valores.append(int(input('Digite um número: ')))
    sleep(0.23)
    count_varios_valores += 1
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
print(f'Foram digitados {count_varios_valores} números')
print(f'Os números digitados foram: {sorted(lista_varios_valores, reverse=True)}') # mostra a lista em ordem decrescente
if 5 in lista_varios_valores:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 82
# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, respectivamente
# Ao final, mostre o conteúdo das três listas geradas
print('-='*35)
print('{:=^81}'.format('\33[30;42mLista pares e ímpares\33[m'))
print('-='*35)

lista_par_impar = []
lista_par = []
lista_impar = []

while True:
    lista_par_impar.append(int(input('Digite um número: ')))
    sleep(0.23)
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break
for aux in lista_par_impar:
    if aux % 2 == 0:
        lista_par.append(aux)
    else:
        lista_impar.append(aux)
print(f'A lista completa é: {sorted(lista_par_impar)}')
print(f'A lista de pares é: {sorted(lista_par)}')
print(f'A lista de ímpares é: {sorted(lista_impar)}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 83
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
# abertos e fechados na ordem correta
print('-='*35)
print('{:=^81}'.format('\33[30;42mValidando expressões matemáticas\33[m'))
print('-='*35)

expressao_matematica = str(input('Digite uma expressão matemática: '))
count_open_parenteses = 0
count_close_parenteses = 0

for aux in range(0, len(expressao_matematica)):
    if expressao_matematica[aux] == '(':
        count_open_parenteses += 1
    elif expressao_matematica[aux] == ')':
        count_close_parenteses += 1
if count_open_parenteses == count_close_parenteses:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')
print('\033[1;30;41m}#{|\033[m' * 20)
