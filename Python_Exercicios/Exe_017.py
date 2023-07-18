#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa
import math
cateto_ad = float(input('Digite o valor do cateto adjacente: '))
cateto_op = float(input('Digite o valor do cateto oposto: '))
hipo1 = (cateto_ad ** 2 + cateto_op ** 2) ** (1/2)
hipo2 = math.hypot(cateto_ad, cateto_op)
hipo3 = math.sqrt(cateto_ad ** 2 + cateto_op ** 2)
print('O valor da hipotenusa é: {:.2f}'.format(hipo1))
print('O valor da hipotenusa é: {:.2f}'.format(hipo2))
print('O valor da hipotenusa é: {:.2f}'.format(hipo3))