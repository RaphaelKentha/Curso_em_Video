#Aula 8; modulo 1; curso em video
#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import
# e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos
#adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} e igual a {}'.format(num, raiz))
print('#'*30)
import random
num_ale = random.randint(1, 10)
print(num_ale)
#sorteia um numero aleatorio ente o range(1, 10)

'''
pip install emoji
import emoji
print(emoji.emojize('Olá mundo :earth_americas:', use_aliases=True))

instalar o modulo emoji
importar o modulo emoji
printar o emoji
nao executei o codigo, pois nao quero o modulo
'''

##########################################################################################

#desafio 016
#crie um programa que leia um numero real qualquer pelo teclado
#e mostre na tela sua porcao inteira
num_real = float(input('Digite um numero real: '))
num_int = int(num_real)
num_real_int = math.trunc(num_real)
print('O numero real: {} tem a parte inteira: {}'.format(num_real, num_int))
print('{:.0f}'.format(num_real))
print('O numero real: {} tem a parte inteira: {}'.format(num_real, num_real_int))
#tres formas de mostrar a parte inteira de um numero real


#desafio 017
#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo, e mostre o valor da hipotenusa
print('Calculo da hipotenusa')
cat_op = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))
hip = math.hypot(cat_op, cat_adj)
hip2 = math.sqrt((cat_op**2)+(cat_adj**2))
hip3 = (cat_op**2 + cat_adj**2)**(1/2)
print('A hipotenusa do triangulo retangulo e: {:.2f}'.format(hip))
print('A hipotenusa do triangulo retangulo e: {:.2f}'.format(hip2))
print('A hipotenusa do triangulo retangulo e: {:.2f}'.format(hip3))


#desafio 018
#leia um angulo e moste seno cosseno e tangente
print('Calculo do seno, cosseno e tangente')
ang = float(input('Digite o angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do angulo {} e: {:.2f}'.format(ang, sen))
print('O cosseno do angulo {} e: {:.2f}'.format(ang, cos))
print('A tangente do angulo {} e: {:.2f}'.format(ang, tan))


#desafio 019
#sorteie um nome dentre uma lista com n nomes
nomes ={}
for i in range(0, 4):
    nomes[i] = input('Digite o nome: ')
print(nomes)
sorteado = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes[sorteado]))

#desafio 020
#agora dos n alunos sorteie e mostres a ordem dos sorteados
nomes1 ={}
for i in range(0, 4):
    nomes1[i] = input('Digite o nome: ')
print(nomes1)
sorteado1 = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes1[sorteado1]))
sorteado2 = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes1[sorteado2]))
sorteado3 = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes1[sorteado3]))
sorteado4 = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes1[sorteado4]))


#desafio 021
#faca o python ler um arquivo mp3
# pip install pygame
#import pygame
#mp3 = pygame.mixer.music.load('musica.mp3')
#teria que instala o pygame, mais nao quero