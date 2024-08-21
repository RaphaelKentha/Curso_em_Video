#desafio 95
# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista_jogadores = list()
dados_jogador = dict()

while True:
    dados_jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    gols = list()
    for aux in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {aux}? ')))
    dados_jogador['gols'] = gols
    dados_jogador['total_gols'] = sum(gols)
    lista_jogadores.append(dados_jogador.copy())
    print('-='*30)
    print(dados_jogador)
    print('-='*30)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('Análise dos dados: ')
for aux in range(len(lista_jogadores)):
    print(f'{aux} ', end='')
    for keys, values in lista_jogadores[aux].items():
        print(f'{keys} = {values}; ', end='')
    print()

while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar_dados == 999:
        break
    if mostrar_dados < len(lista_jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogadores[mostrar_dados]["nome"]}: ')
        for aux, gols in enumerate(lista_jogadores[mostrar_dados]['gols']):
            print(f'No jogo {aux + 1} fez {gols} gols.')
    else:
        print('Erro! Jogador não encontrado.')
