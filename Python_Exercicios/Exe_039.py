# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano # date.today().year pega o ano atual
sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    if idade < 18:
        print('Você ainda vai se alistar.')
        print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(ano + 18))
    elif idade == 18:
        print('Você deve se alistar imediatamente.')
    else:
        print('Você já deveria ter se alistado.')
        print('Você está {} anos atrasado.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(ano + 18))
else:
    print('Você não precisa se alistar.')

# meu codigo:
'''
from time import sleep
from datetime import date
print('=$'*40)
print('\t\t\t\33[30;42mAlistamento Militar\33[m')
print('=$'*40)
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
print('Aguarde...')
sleep(1)
ano_atual = date.today().year #ano atual
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você ainda não tem 18 anos, faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você tem 18 anos, está na hora de se alistar.')
else:
    print('Você já passou da idade de se alistar, passaram {} anos.'.format(idade - 18))
print('=$'*40)
'''