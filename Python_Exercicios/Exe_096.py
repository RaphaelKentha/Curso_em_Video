#desafio 96
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
#  (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A largura do terreno é {largura}m e o comprimento é {comprimento}m, a área do terreno é {area}m²')


print('Calculando a area de um terreno')
largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite o comprimento do terreno em metros: '))
area(largura, comprimento)