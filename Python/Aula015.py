#aula 15; modulo 2; curso em video
# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos 
# a favor das nossas estratégias de código. É muito importante saber usar o break no Python,
# já que em alguns casos precisamos interromper um laço no meio do caminho
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python

numero_cont = soma = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        break
    soma += numero
    numero_cont += 1
print(f'A soma vale {soma}')
print(f'Foram digitados {numero_cont} números') # print usando fstring
print('Foram digitados {} números'.format(numero_cont)) # print usando format

#desafio 66
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando 
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag)

from time import sleep
print('-='*35)
print('{:=^81}'.format('\33[30;42mLer numero\33[m'))
print('-='*35)
print('Digite 999 para parar')
somo66 = 0
conta66 = 0
while True:
    numero66 = int(input('Digite um número: '))
    if numero66 == 999:
        break
    somo66 += numero66
    conta66 += 1
print('Finalizando...')
sleep(1)
print(f'A soma dos {conta66} números digitados é {somo66}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 67
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
print('-='*35)
print('{:=^81}'.format('\33[30;42mTabuada\33[m'))  
print('-='*35)

numero_tabuada = 0

while True:
    numero_tabuada = int(input('Digite um número para ver sua tabuada: '))
    if numero_tabuada < 0:
        break
    for aux in range(1, 11):
        print(f'{numero_tabuada} x {aux} = {numero_tabuada * aux}')
        sleep(0.3)
print('Finalizando...')
sleep(1)
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 68
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random

print('-='*35)
print('{:=^81}'.format('\33[30;42mPar ou Impar\33[m'))
print('-='*35)

numero_vitorias = 0

while True:
    mao_jogador = int(input('Digite um número de 0 a 5: '))
    par_impar = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    mao_pc = random.randint(0, 5)
    print("PAR..")
    sleep(0.3)
    print("OU..")
    sleep(0.3)
    print("IMPAR..")
    sleep(0.3)
    if (mao_pc + mao_jogador) % 2 == 0 and par_impar == 'P':
        numero_vitorias += 1
        print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU PAR')
        print('Você VENCEU!')
    elif (mao_pc + mao_jogador) % 2 != 0 and par_impar == 'I':
        numero_vitorias += 1
        print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU IMPAR')
        print('Você VENCEU!')
    else:
        if par_impar == 'P':
            print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU IMPAR')
            print('Você PERDEU!')
        else:
            print(f'Você jogou {mao_jogador} e o computador {mao_pc}. Total de {mao_pc + mao_jogador} DEU PAR')
            print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {numero_vitorias} vezes.')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 69
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

print('-='*35)
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

#desafio 70
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

print('-='*35)
print('{:=^81}'.format('\33[30;42mLoja\33[m'))
print('-='*35)


total_gasto =0
contador_mais1000 = 0
contador = 0
valor_produto =0

while True:
    nome_produto = str(input('Nome do produto: ')).strip().upper()
    valor_produto = float(input('Preço do produto: R$'))
    contador += 1
    total_gasto += valor_produto
    if valor_produto > 1000:
        contador_mais1000 += 1
    if contador == 1:
        nome_produto_barato = nome_produto
        valor_produto_barato = valor_produto
    elif valor_produto < valor_produto_barato:
        nome_produto_barato = nome_produto
        valor_produto_barato = valor_produto
    continuar_val = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar_val == 'N':
        break
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {contador_mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto_barato} que custa R${valor_produto_barato:.2f}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 71
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('-='*35)
print('{:=^81}'.format('\33[30;42mCaixa Eletrônico\33[m'))
print('-='*35)

valor_saque = int(input('Qual valor você quer sacar? R$'))
notas50 = notas20 = notas10 = notas1 = 0

if valor_saque < 1:
    print('Valor inválido')
elif valor_saque > 50:
    notas50 = valor_saque // 50
    valor_saque = valor_saque % 50
    if valor_saque > 20:
        notas20 = valor_saque // 20
        valor_saque = valor_saque % 20
        if valor_saque > 10:
            notas10 = valor_saque // 10
            valor_saque = valor_saque % 10
            if valor_saque > 1:
                notas1 = valor_saque // 1
                valor_saque = valor_saque % 1
        else:
            notas1 = valor_saque // 1
            valor_saque = valor_saque % 1
    else:
        notas1 = valor_saque // 1
        valor_saque = valor_saque % 1
    print(f'Total de {notas50} cédulas de R$50')
    print(f'Total de {notas20} cédulas de R$20')
    print(f'Total de {notas10} cédulas de R$10')
    print(f'Total de {notas1} cédulas de R$1')
elif valor_saque > 20 and valor_saque <= 50:
    if valor_saque == 50:
        print(f'Total de {1} cédula de R$50')
    elif valor_saque < 50:
        notas20 = valor_saque // 20
        valor_saque = valor_saque % 20
        if valor_saque > 10:
            notas10 = valor_saque // 10
            valor_saque = valor_saque % 10
            if valor_saque > 1:
                notas1 = valor_saque // 1
                valor_saque = valor_saque % 1
        else:
            notas1 = valor_saque // 1
            valor_saque = valor_saque % 1
    print(f'Total de {notas20} cédulas de R$20')
    print(f'Total de {notas10} cédulas de R$10')
    print(f'Total de {notas1} cédulas de R$1')
elif valor_saque > 10 and valor_saque <= 20:
    if valor_saque == 20:
        print(f'Total de {1} cédula de R$20')
    elif valor_saque < 20:
        notas10 = valor_saque // 10
        valor_saque = valor_saque % 10
        if valor_saque > 1:
            notas1 = valor_saque // 1
            valor_saque = valor_saque % 1
    print(f'Total de {notas10} cédulas de R$10')
    print(f'Total de {notas1} cédulas de R$1')
elif valor_saque >= 1 and valor_saque <= 10:
    if valor_saque == 10:
        print(f'Total de {1} cédula de R$10')
    elif valor_saque < 10:
        notas1 = valor_saque // 1
        valor_saque = valor_saque % 1
    print(f'Total de {notas1} cédulas de R$1')
print('\033[1;30;41m}#{|\033[m' * 20)
