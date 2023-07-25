# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
if (valor_casa / (anos * 12)) > (salario * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
    print('Você pagará R${:.2f} por mês.'.format(valor_casa / (anos * 12)))

# meu codigo:
'''
import time
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mEmpréstimo Bancário\33[m')
print('=$'*40)
print('Para realizar o empréstimo, precisamos de algumas informações: ')
valor_casa = float(input('Qual o valor da casa? R$: '))
print('Aguarde...')
sleep(1)
valor_salario = float(input('Qual o valor do seu salário? R$: '))
print('Aguarde...')
sleep(1)
finaceamento_anos = int(input('Em quantos anos você pretende pagar? ')) #adotando que o tempo maximo de financiamento é de 30 anos
print('Aguarde...')
sleep(1)
print('Calculando...')
sleep(3)
valor_da_prestacao = valor_casa / (finaceamento_anos * 12)
if valor_da_prestacao <= (valor_salario * 0.3) and finaceamento_anos <= 30 and valor_da_prestacao > 0 and valor_casa > 0 and valor_salario > 0:
    print('\33[30;42mParabéns, seu empréstimo foi aprovado!\33[m')
    print('O valor da prestação será de R$ {:.2f}'.format(valor_da_prestacao))
else:
    print('\33[0;30;41mInfelizmente seu empréstimo não foi aprovado.\33[m')
    print('O valor da prestação seria de R$ {:.2f}'.format(valor_da_prestacao))
print('=$'*40)
'''