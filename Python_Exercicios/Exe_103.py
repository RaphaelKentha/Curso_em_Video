#desfio 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou

nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols ele marcou: '))

def ficha_fogador(nome = 'NoName', gols = 0):
    if nome == '':
        nome = 'NoName'
    if gols == '':
        gols = 0
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

ficha_fogador(nome, gols)
