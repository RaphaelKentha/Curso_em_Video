# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e está na categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER.'.format(idade))

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mCategoria de Natação\33[m')
print('=$'*40)
nome_do_atleta = input('Digite o nome do atleta: ').strip().capitalize()
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year #ano atual
idade_do_atleta = ano_atual - ano_nascimento
print('Pocesando...')
if idade_do_atleta <= 9:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;42mMIRIM\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 9 and idade_do_atleta <= 14:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;43mINFANTIL\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 14 and idade_do_atleta <= 19:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;44mJUNIOR\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 19 and idade_do_atleta <= 25:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;45mSÊNIOR\33[m.'.format(nome_do_atleta, idade_do_atleta))
else:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;46mMASTER\33[m.'.format(nome_do_atleta, idade_do_atleta))
print('=$'*40)
'''