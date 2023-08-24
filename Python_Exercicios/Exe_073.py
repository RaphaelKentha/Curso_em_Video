# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# Os 5 primeiros times
# Os últimos 4 colocados
# Times em ordem alfabética
# Em que posição está o time da Chapecoense

tupla_campeonato = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
                     'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
                       'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
                         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(' Os 5 primeiros times:')
for aux in range(0, 5):
    print(f'{aux+1}º {tupla_campeonato[aux]}')
print('Lanternas:')
for aux in range(16, 20):
    print(f'{aux+1}º {tupla_campeonato[aux]}')
print('Times em ordem alfabética:')
print(sorted(tupla_campeonato), end = ' ') # sorted() retorna uma lista ordenada com os elementos da tupla
print('\n')
print('Em que posição está o time da Chapecoense:')
for aux in range(0, 20):
    if tupla_campeonato[aux] == 'Chapecoense':
        print(f'{aux+1}º {tupla_campeonato[aux]}')
        break

# meu codigo:
'''
from time import sleep

print('-='*35)
print('{:=^81}'.format('\33[30;42mTabela do Brasileirão\33[m'))
print('-='*35)
tupla_brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Os times em ordem alfabética são:')
print('Processando...')
sleep(1)
print(sorted(tupla_brasileirao))
print('-='*35)
for aux in range(0, len(tupla_brasileirao)):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.15)
print('-='*35)
print('Processando...')
sleep(1)
print(f'Os 5 primeiros colocados são:')
for aux in range(0, 5):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.09)
print('-='*35)
print('Processando...')
sleep(1)
print(f'Os 4 últimos colocados são:')
for aux in range(16, 20):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.09)
print('-='*35)
print('Processando...')
sleep(1)
print('Posição da Chapecoense:')
if 'Chapecoense' in tupla_brasileirao:
    print(f'Está na {tupla_brasileirao.index("Chapecoense")+1}ª posição')
print('\033[1;30;41m}#{|\033[m' * 20)
'''