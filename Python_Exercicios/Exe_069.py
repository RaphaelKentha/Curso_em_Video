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


