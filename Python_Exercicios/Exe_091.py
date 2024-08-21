#desafio 91
# Crie um programa onde 4 jogadores joguem um dado 
# e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.
import random

jogadores = dict()

for aux in range(1, 5):
    jogadores[f'jogador{aux}'] = random.randint(1, 6)
    #adiciona o jogador e o valor do dado ao dicionário

for keys, values in jogadores.items():
    print(f'{keys} tirou {values} no dado')

print('Ranking dos jogadores: ')
for keys, values in enumerate(sorted(jogadores.values(), reverse=True)):
    #sorted() retorna os valores do dicionário em ordem
    #reverse=True inverte a ordem
    print(f'{keys + 1}º lugar: {values}')

for keys, values in jogadores.items():
    if values == max(jogadores.values()):
        #verifica se o valor é o maior do dicionário
        #max() retorna o maior valor do dicionário
        print(f'{keys} tirou {values} e é o vencedor')
