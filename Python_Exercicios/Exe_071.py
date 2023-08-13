# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
total_ced = 0


while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

# meu codigo:
'''
from time import sleep
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

kkkkkkk :)
'''