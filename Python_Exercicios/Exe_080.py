# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_cinco = []

for aux in range(0, 5):
    numero = int(input('Digite um número: '))
    if len(lista_cinco) == 0:
        lista_cinco.append(numero)
    else:
        for contador in range(0, len(lista_cinco)):
            if numero <= lista_cinco[contador]: # se o numero for menor ou igual ao numero na posição contador
                lista_cinco.insert(contador, numero) # insere o numero na posição contador
                break
            elif numero > lista_cinco[-1]: # se o numero for maior que o ultimo numero da lista
                lista_cinco.append(numero)
                break
print(f'Os valores digitados foram: {lista_cinco}')

# meu codigo:
'''
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
'''