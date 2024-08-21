#desafio 90
# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

registro = dict()
nome = str(input('Nome: '))
media = float(input('Média: '))
registro['nome'] = nome # adiciona o nome ao dicionário
registro['media'] = media # adiciona a média ao dicionário
if media >= 7:
    situacao = 'Esta Aprovado'
    registro['situacao'] = situacao # adiciona a situação ao dicionário
else:
    situacao = 'Esta Reprovado'
    registro['situacao'] = situacao
for keys, values in registro.items():
    print(f'{keys} = {values}')