# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

fatorial_numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial_resultado = 1

for aux in range(fatorial_numero, 0, -1):
    fatorial_resultado *= aux
    print(aux, end=' ')
    print('x' if aux > 1 else ':', end=' ') # if inline para printar o x e : no final
print(fatorial_resultado)

# fiz usando o for, pois o while nao foi necessario
# meu codigo com while:
'''	
from time import sleep
import math

# usando o modulo math:
fatorial_numero = int(input('Digite um numero para saber seu fatorial: '))
print('Aguarde...')
sleep(0.5)
print('O fatorial de {} é {}'.format(fatorial_numero, math.factorial(fatorial_numero)))
print('\033[1;30;41m}#{|\033[m' * 20)

fatorial_numero = int(input('Digite um numero para saber seu fatorial: '))
aux_fatorial = 0
operaca_fatorial = 1
while aux_fatorial != fatorial_numero:
    operaca_fatorial *= fatorial_numero - aux_fatorial
    aux_fatorial += 1
print('Aguarde...')
sleep(0.5)
print('O fatorial de {} é {}'.format(fatorial_numero, operaca_fatorial))
print('\033[1;30;41m}#{|\033[m' * 20)
'''