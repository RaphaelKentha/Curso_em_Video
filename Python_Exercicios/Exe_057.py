# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto

sexo_while = False

while sexo_while == False:
    sexo_pessoa = str(input('Digite o sexo da pessoa [M/F]: ')).upper()[0]
    if sexo_pessoa == 'M' or sexo_pessoa == 'F':
        if sexo_pessoa == 'M':
            print('Sexo Masculino')
        else:
            print('Sexo Feminino')
        sexo_while = True
    else:
        print('Sexo inválido, digite novamente!\n################################')

# meu codigo:
'''	
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mValidação de dados\33[m'))
print('=#' * 35)
validacao = 0
while validacao == 0:
    sexo_user = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if sexo_user =='M' or sexo_user == 'F':
        validacao = 1
        print('Aguarde...')
        sleep(0.5)
        if sexo_user == 'M':
            print('Você é do sexo Masculino')
        else:
            print('Você é do sexo Feminino')
print('Fim do programa')
print('\033[1;30;41m}#{|\033[m' * 20)
'''	