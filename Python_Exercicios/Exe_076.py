# Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular

tupla_produto_preco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
                          'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
                            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for aux in range(0, len(tupla_produto_preco)):
    if aux % 2 == 0:
        print(f'{tupla_produto_preco[aux]:.<30}', end = '')
    else:
        print(f'R${tupla_produto_preco[aux]:>7.2f}')
print('-'*40)

# meu codigo:
'''
from time import sleep

print('-='*35)
print('{:=^81}'.format('\33[30;42mListagem de preços\33[m'))
print('-='*35)

tupla_produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for aux in range(0, len(tupla_produtos), 2):
    sleep(0.17)
    print(f'{tupla_produtos[aux]:.<30}R$ {tupla_produtos[aux+1]:>7.2f}') # :.<30 alinha a esquerda com 30 caracteres e :>7.2f alinha a direita com 7 caracteres e 2 casas decimais
print('\033[1;30;41m}#{|\033[m' * 20)
'''
