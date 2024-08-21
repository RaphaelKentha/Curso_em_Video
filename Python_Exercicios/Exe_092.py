#desafio 92
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ano_atual = datetime.now().year
#usando a biblioteca datetime para pegar o ano atual

cadastro_trabalhador = dict()

nome = cadastro_trabalhador['nome'] = str(input('Nome: '))
ano_nascimento = cadastro_trabalhador['ano_nascimento'] = int(input('Ano de nascimento: '))
idade = cadastro_trabalhador['idade'] = ano_atual - ano_nascimento
ctps = cadastro_trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if ctps != 0:
    cadastro_trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro_trabalhador['salario'] = float(input('Salário: R$ '))
    cadastro_trabalhador['aposentadoria'] = cadastro_trabalhador['ano_contratacao'] + 35 - ano_nascimento

for keys, values in cadastro_trabalhador.items():
    print(f'{keys}: {values}')