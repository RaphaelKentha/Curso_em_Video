# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado_1 = float(input('Digite o primeiro lado do triangulo: '))
lado_2 = float(input('Digite o segundo lado do triangulo: '))
lado_3 = float(input('Digite o terceiro lado do triangulo: '))
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Os lados digitados formam um triangulo')
else:
    print('Os lados digitados nao formam um triangulo')
print('Fim do programa')

# Meu codigo abaixo:
'''
# Leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
lado_a = float(input('Digite o comprimento do lado A: '))
lado_b = float(input('Digite o comprimento do lado B: '))
lado_c = float(input('Digite o comprimento do lado C: '))
lados_triangulo = [lado_a, lado_b, lado_c]
existencia_triangulo = sum(lados_triangulo) - max(lados_triangulo)
if existencia_triangulo > max(lados_triangulo):
    print('Os lados formam um triangulo')
else:
    print('Os lados nao formam um triangulo')
print('Fim do programa')
print('#' * 50)
'''	