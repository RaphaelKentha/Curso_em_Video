#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o valor do angulo: '))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print('O valor do seno é: {:.2f}'.format(seno))
print('O valor do cosseno é: {:.2f}'.format(cosseno))
print('O valor da tangente é: {:.2f}'.format(tangente))
