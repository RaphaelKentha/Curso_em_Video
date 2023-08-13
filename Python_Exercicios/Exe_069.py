# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

numero_mais18 = 0
numero_homem = 0
numero_mulher = 0
numero_pessoas = 0
continuar = 'S'

while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    numero_pessoas += 1
    if idade > 18:
        numero_mais18 += 1
    elif sexo == 'M':
        numero_homem += 1
    elif sexo == 'F' and idade < 20:
        numero_mulher += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {numero_pessoas} pessoas')
print(f'{numero_mais18} pessoas tem mais de 18 anos')
print(f'{numero_homem} homens foram cadastrados')
print(f'{numero_mulher} mulheres tem menos de 20 anos')

# meu codigo:
'''
from time import sleep
cprint('-='*35)
print('{:=^81}'.format('\33[30;42mCadastro de pessoas\33[m'))
print('-='*35)

contador_mais18 = contador_homens = contador_mulheres_menos20 = 0
continuar_val = 'S'
while True:
    nome_pessoa = str(input('Nome: ')).strip().upper()
    sexo_pessoa = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade_pessoa = int(input('Idade: '))
    if sexo_pessoa == 'M':
        if idade_pessoa >= 18:
            contador_mais18 += 1
            contador_homens += 1
        else:
            contador_homens += 1
    elif sexo_pessoa == 'F' and idade_pessoa < 20:
        contador_mulheres_menos20 += 1
    elif sexo_pessoa == 'F' and idade_pessoa >= 18:
        contador_mais18 += 1
    continuar_val = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar_val == 'N':
        break
    else:
        print('Não entendi, digite novamente')
print(f'Total de pessoas com mais de 18 anos: {contador_mais18}')
print(f'Ao todo temos {contador_homens} homens cadastrados')
print(f'E temos {contador_mulheres_menos20} mulheres com menos de 20 anos')
print('\033[1;30;41m}#{|\033[m' * 20)
'''


