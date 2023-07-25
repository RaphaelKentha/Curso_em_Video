# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados acima podem formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os lados acima não podem formar um triângulo.')

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mAnalisador de Triângulos\33[m')
print('=$'*40)
lado_a = float(input('Digite o comprimento do lado A: '))
lado_b = float(input('Digite o comprimento do lado B: '))
lado_c = float(input('Digite o comprimento do lado C: '))
print('Calculando...')
sleep(1)
lados_triangulo = [lado_a, lado_b, lado_c]
existencia_triangulo = sum(lados_triangulo) - max(lados_triangulo)
if existencia_triangulo > max(lados_triangulo):
    print('Os lados formam um triangulo')
    if lado_a == lado_b and lado_a == lado_c:
        print('O triangulo é \33[0;30;42mEQUILÁTERO\33[m.')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('O triangulo é \33[0;30;43mISÓSCELES\33[m.')
    else:
        print('O triangulo é \33[0;30;44mESCALENO\33[m.')
else:
    print('Os lados nao formam um triangulo')
print('Fim do programa')
print('=$'*40)
'''	