#desafio 101
# Crie um programa que tenha uma função chamada voto()
#  que vai receber como parâmetro o ano de nascimento de uma pessoa,
#  retornando um valor literal indicando se uma pessoa tem voto NEGADO,
#  OPCIONAL e OBRIGATÓRIO nas eleições

from datetime import date


def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    #calcula a idade usando a data atual
    #usando a data atual, importada da biblioteca time
    if 16 <= idade < 18 or idade > 70:
        print('VOTO OPCIONAL')
    elif 18 <= idade < 70:
        print('VOTO OBRIGATÓRIO')
    else:
        print('VOTO NEGADO')

pessoa = int(input('Digite o ano de nascimento: '))
voto(pessoa)