#desfio 89
# Crie um programa que leia nome e duas notas de vários alunos 
# e guarde tudo em uma lista composta. No final, mostre um boletim 
# contendo a média de cada um e permita que o usuário possa mostrar 
# as notas de cada aluno individualmente.

boletim = []
aluno_nome_notas = []

while True:
    aluno_nome_notas.append(str(input('Nome: ')))
    aluno_nome_notas.append(float(input('Nota 1: ')))
    aluno_nome_notas.append(float(input('Nota 2: ')))
    boletim.append(aluno_nome_notas[:])
    aluno_nome_notas.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print("=-" * 30)
for aux in range(0, len(boletim)):
    media = (boletim[aux][1] + boletim[aux][2]) / 2
    print(f'Aluno {aux+1}: {boletim[aux][0]} - Média: {media}')

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if aluno == 999:
        break
    print(f'Notas de {boletim[aluno - 1][0]} são {boletim[aluno - 1][1:]}')
    print("=-" * 30)