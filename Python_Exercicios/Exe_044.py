# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e 
# condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros
valor_produto = float(input('Qual o valor do produto? R$'))
print('Qual a forma de pagamento?')
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('O valor do produto com desconto será de R${:.2f}'.format(valor_produto * 0.9))
elif opcao == 2:
    print('O valor do produto com desconto será de R${:.2f}'.format(valor_produto * 0.95))
elif opcao == 3:
    print('O valor do produto será de R${:.2f}'.format(valor_produto))
elif opcao == 4:
    print('O valor do produto com juros será de R${:.2f}'.format(valor_produto * 1.2))
else:
    print('Opção inválida. Tente novamente.')

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mCalculadora de Preços\33[m')
print('=$'*40)
numero_de_parcelas = 0
preco_do_produto = float(input('Digite o preço do produto: R$ '))
tipo_de_pagamento = int(input('Digite o tipo de pagamento: \n1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão\nEscolha: '))
print('Processando...')
sleep(2)
if tipo_de_pagamento == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco_do_produto * 0.9))
elif tipo_de_pagamento == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco_do_produto * 0.95))
elif tipo_de_pagamento == 3:
    print('O valor a ser pago é de R$ {:.2f} em 2X'.format(preco_do_produto / 2))
elif tipo_de_pagamento == 4:
    numero_de_parcelas = int(input('Digite o número de parcelas: '))
    print('O valor a ser pago é de R$ {:.2f} em {}X'.format(((preco_do_produto * 1.2) / numero_de_parcelas) , numero_de_parcelas))
print('=$'*40)
'''