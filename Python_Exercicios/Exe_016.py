#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
#Ex: Digite um número: 6.127
import math
num_real = float(input('Digite um numero real: '))
num_int = int(num_real)
num_real_int = math.trunc(num_real)
print('O numero real: {} tem a parte inteira: {}'.format(num_real, num_int))
print('{:.0f}'.format(num_real))
print('O numero real: {} tem a parte inteira: {}'.format(num_real, num_real_int))
#tres formas de mostrar a parte inteira de um numero real
