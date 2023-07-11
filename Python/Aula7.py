#Aula 7 modulo 1
#operadores aritmeticos
# **; *; /; //; %; +; -;
#expo; multi; divi; divi_int; resto; adicao; subtracao

#aplicando os tipos de operadores aritmeticos

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite um valor: '))
soma = v1 + v2
sub = v1 - v2
mul = v1 * v2
div_int = v1 // v2
div = v1 / v2
exp = v1 ** v2
resto = v1 % v2

print('A soma é: {}'.format(soma))
print('A subtração é: {}'.format(sub))
print('A multiplicação é: {}'.format(mul))
print('A divisão por inteiro é: {}'.format(div_int))
print('A divisão é: {}'.format(div))
print('A exponenciação é: {}'.format(exp))
print('A sobra da divisão é: {}'.format(resto))
#a função print, tem outras formas de deixar a saida mais bonita

#desafio 005 e006
#faça um programa que leia um numero inteiro e mostre na saida
#o numero digitado, seu sucessor e seu antecessor, mostre o valor
#do seu dobro, triplo e sua raiz quadrada

num_int = int(input('Digite um numero inteiro: '))
print('Passo define a razão de saida do programa!')
passo = int(input('Defina o passo: '))
num_int_suc = (num_int + passo)
num_int_ant = (num_int - passo)
num_int_tri = (num_int * 3)
num_int_dob = (num_int * 2)
num_int_raiz = (num_int ** 0,5)
print('O numero escolhido e: {} \nSeu sucessor e: {} \nSeu antecessor e: {}'.format(num_int, num_int_suc, num_int_ant))
print('O dobro e: {} \nO triplo e: {} \nA raiz quadrada e: {}'.format(num_int_tri, num_int_dob, num_int_raiz))
print(num_int_raiz)
print(type(num_int_raiz))
#desafio 007
#receba duas notas e mostre a media
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
print('Media da notas: {}'.format(media))
#desafio 008
#receba um valor em metros e conveta para cm e mm
val_metros = float(input('Digite um valor em metros: '))
val_centimetros = val_metros * 100
val_milimetros = val_centimetros * 100
print('O valor: {} em metros, equivale: \nA {} centimetros \nA {} milimetros'.format(val_metros, val_centimetros, val_milimetros))
#desafio 009
#receba um numero inteiro, e mostre sua respectiva tabuada
tabu_val = int(input('Digite sua tabuada: '))
tab1 = (1 * tabu_val)
tab2 = (2 * tabu_val)
tab3 = (3 * tabu_val)
tab4 = (4 * tabu_val)
tab5 = (5 * tabu_val)
tab6 = (6 * tabu_val)
tab7 = (7 * tabu_val)
tab8 = (8 * tabu_val)
tab9 = (9 * tabu_val)
tab10 = (10 * tabu_val)
#exite laço de repetçao!!!!
print('1 X {} = {} \n2 X {} = {} \n3 X {} = {} \n4 X {} = {} \n5 X {} = {} \n6 X {} = {} \n7 X {} = {} \n8 X {} = {} \n9 X {} = {} \n10 X {} = {}'.format(tabu_val, tab1, tabu_val, tab2, tabu_val, tab3, tabu_val, tab4, tabu_val, tab5, tabu_val, tab6, tabu_val, tab7, tabu_val, tab8, tabu_val, tab9, tabu_val, tab10))
#desafio 010
#converta certa quantidade de R$ para US$
#desafio 011
#calcule a area em m², e diga a quntidade de litros de tinta nescessario para esta area
#sendo 1l de tinta, pinta 2m²
#desafio 0012
#leia o preço de um produto, e mostre seu valor com x% de desconto
#desafio 012
#calcule o salario com x% de aumento

#nota: depois vou concluir os defaios restantes