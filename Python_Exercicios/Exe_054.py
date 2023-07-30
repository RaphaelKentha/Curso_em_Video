# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
count_maioridade = 0
ano_atual = date.today().year# ano atual
for aux in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(aux)))
    if ano_atual - ano_nascimento >= 21:
        count_maioridade += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(count_maioridade))
print('E também tivemos {} pessoas menores de idade.'.format(7 - count_maioridade))

# meu codigo:
'''
from datetime import date
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mMaioridade\33[m'))
print('=#' * 35)
from datetime import date
ano_atual = date.today().year # pega o ano atual
lista_ano_nascimento = []
maioridade = 0
print('Digite o ano de nascimento de 6 pessoas: ')
for aux in range(0, 6):
    ano_nascimento = int(input('Digite o ano de nascimento da pessoa {}: '.format(aux + 1)))
    lista_ano_nascimento.append(ano_nascimento)
len_lista_ano_nascimento = len(lista_ano_nascimento)
for aux in range(0, len_lista_ano_nascimento):
    if ano_atual - lista_ano_nascimento[aux] >= 18:
        maioridade += 1
print('Processando ...')
sleep(2)
print('Das {} pessoas, {} são maiores de idade e {} são menores de idade.'.format(len_lista_ano_nascimento, maioridade, len_lista_ano_nascimento - maioridade))
print ('\033[1;30;41m}#{|\033[m' * 20)
'''