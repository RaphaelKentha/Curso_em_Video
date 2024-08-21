#desafio 93
#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados_jogador = dict()

while True:
    dados_jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    gols = list()
    for aux in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {aux}? ')))
    dados_jogador['gols'] = gols
    dados_jogador['total_gols'] = sum(gols)
    print('-='*30)
    print(dados_jogador)
    print('-='*30)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break