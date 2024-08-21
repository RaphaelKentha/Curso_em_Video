#desafio 94
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

lista_pessoas = list()

somatorio_idade = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somatorio_idade += pessoa['idade']
    lista_pessoas.append(pessoa)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
numero_pessoas = len(lista_pessoas)
media_idade = somatorio_idade / numero_pessoas

print(f'Foram cadastradas {numero_pessoas} pessoas.')
print(f'A média de idade é {media_idade} anos.')

for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'F':
        print(f'As mulheres cadastradas foram: {pessoa["nome"]}')

for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idade:
        print(f'As pessoas com idade acima da média são: {pessoa["nome"]}')