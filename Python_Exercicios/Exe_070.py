# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de R$1000
# qual é o nome do produto mais barato

total_gasto = 0
mais1000 = 0
nome_barato = ''
preco_barato = 0
continuar = 'S'
contador = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip().title() # title() para deixar a primeira letra maiuscula
    preco = float(input('Digite o preço do produto: R$'))
    total_gasto += preco
    contador += 1
    if preco > 1000:
        mais1000 += 1
    if contador == 1:
        nome_barato = nome
        preco_barato = preco
    else:
        if preco < preco_barato:
            nome_barato = nome
            preco_barato = preco
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'{mais1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {nome_barato} que custa R${preco_barato:.2f}')

# meu codigo:
'''	
from time import sleep

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
'''	