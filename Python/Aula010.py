# Aula 10; modulo 1; curso em video
# |Condições em Python (if..else)| #
# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e 
# compostas nos seus programas em Python.

nome = input('Digite seu nome: ').strip().capitalize()
if nome.capitalize() == "Raphael":
    print('Que nome lindo voce tem!')
else:
    print('oK, seu nome é {}'.format(nome))
print('Bom dia')

#if simplificado: existe, mais nao e pytonico
#print('Que nome lindo voce tem!' if nome.capitalize() == "Raphael" else 'oK, seu nome é {}'.format(nome))

# usando if, para ver o desem penho de uma escola de samba
nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))
nota3 = float(input('Digite a nota: '))
nota4 = float(input('Digite a nota: '))
nota5 = float(input('Digite a nota: '))
lista_notas = [nota1, nota2, nota3, nota4, nota5]
nota_maxima = max(lista_notas)
nota_minima = min(lista_notas)
#nas notas de escolas de samba, se excluem a maior e a menor nota
nota_avaliacao = (nota1 + nota2 + nota3 + nota4 + nota5 - nota_maxima - nota_minima) / 3
print('#' * 50)
print('A nota de avaliacao da escola de samba e: {}'.format(nota_avaliacao))
if nota_avaliacao >= 9.0:
    print("A escola de samba e EXELENTE")
elif nota_avaliacao >= 7.0:
    print("A escola de samba e BOA")
elif nota_avaliacao >= 5.0:
    print("A escola de samba e RAZOAVEL")
else:
    print("A escola de samba e PESSIMA")
    print('Deve ser rebaixada')
print('#' * 50)
print('#' * 50)
print('\t\t#Desafios#')
print('#' * 50)

#desafio 028
# Escreva um programa que faca o computador "pensar"
# em um numero inteiro no intervalo de [0 - 5]
# e paca para o usuario tentar descobrir qual foi o numero
# e ob resultado devera ser exibido na tela
import random

numeros_sorteados = random.randint(0, 5) # sorteia um numero inteiro entre 0 e 5
numero_do_usuario = int(input('Digite um numero inteiro entre 0 e 5: '))
if numero_do_usuario == numeros_sorteados:
    print('Parabens, voce acertou')
else:
    print('Que pena, voce errou')
print('O numero sorteado foi: {}'.format(numeros_sorteados))
print('O numero digitado: {}'.format(numero_do_usuario))
print('Fim do programa')
print('#' * 50)

#desafio 029
'''
Leia a velocidade de um carro na estrada
se o mesmo ultrapassar 80 Km/h ele sera multado em 69 reais
por cada km/h acima do limite permitido.
'''
velocidado_do_veiculo = float(input('Digite a velocidade do veiculo: '))
print('A velocidade maxima permitida e: 80 Km/h')
if velocidado_do_veiculo <= 80 and velocidado_do_veiculo >0:
    print('Parabens, voce esta dentro da velocidade permitida')
elif velocidado_do_veiculo > 80:
    print('Sua velocidade e: {} Km/h'.format(velocidado_do_veiculo))
    print('Voce foi multado em: {:.1f} Reai$'.format((velocidado_do_veiculo - 80) * 69,73))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)

#desafio 030
# Leia um numero e indique se ele e par ou impar
import math

leia_numero = int(input('Digite um numero inteiro: '))
if math.fmod(leia_numero, 2) == 0: # verifica se o resto da divisao e igual a zero
    print('O numero {} e par'.format(leia_numero))
else:
    print('O numero {} e impar'.format(leia_numero))
# usando o fmod, e possivel verificar se um numero e par ou impar
# pois o mesmo retorna o resto da divisao
print('Fim do programa')
print('#' * 50)

#desafio 031
'''
 Calcule o preco de uma viagem, de acordo com a distancia percorrida
ate 200km, o km e cinquenta centavos acima de 200km o km e quarenta e cinco cents de dolar.
'''
viagem_km = float(input('Digite a distancia da viagem em km: '))
valor_dollar = float(input('Digite o valor do dolar: '))
if viagem_km > 0 and viagem_km <= 200:
    print('O valor da viagem e: {:.2f} Reai$'.format(viagem_km * 0.5))
elif viagem_km > 200:  
    print('O valor da viagem e: {:.2f} Reai$'.format(viagem_km * 0.45*valor_dollar))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)

#desafio 032
# Leia o ano corrente, e decubra se o mesmo e bissexto

ano_corrente = int(input('Digite o ano corrente: '))
if math.fmod(ano_corrente, 4) == 0 and math.fmod(ano_corrente, 100) != 0 or math.fmod(ano_corrente, 400) == 0:
    print('O ano {} e bissexto'.format(ano_corrente))
else:
    print('O ano {} nao e bissexto'.format(ano_corrente))

import calendar

if calendar.isleap(ano_corrente) == True:
    print('O ano {} e bissexto'.format(ano_corrente))
else:
    print('O ano {} nao e bissexto'.format(ano_corrente))
print('Fim do programa')
print('#' * 50)

#desafio 033
# Leia tres numeros e mostre qual e o maior e qual e o menor
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))
lista_numeros = [numero1, numero2, numero3]
print('O maior numero e: {}'.format(max(lista_numeros)))
print('O menor numero e: {}'.format(min(lista_numeros)))
print('#' * 50)
if numero1 > numero2 and numero1 > numero3:
    print('O maior numero e: {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O maior numero e: {}'.format(numero2))
else:
    print('O maior numero e: {}'.format(numero3))
if numero1 < numero2 and numero1 < numero3:
    print('O menor numero e: {}'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('O menor numero e: {}'.format(numero2))
else:
    print('O menor numero e: {}'.format(numero3))
print('Fim do programa')
print('#' * 50)

#desafio 034
# Leia o salario de um funcionario e calcule o aumento
# para salarios superiores a 1250,00 o aumento e de 10%
# para salarios inferiores ou iguais a 1250,00 o aumento e de 15%
leia_salario = float(input('Digite o salario do funcionario: '))
if leia_salario > 0 and leia_salario <= 1250:
    print('O salario do funcionario apos o aumento e: {:.2f} Reai$'.format(leia_salario * 1.15))
elif leia_salario > 1250:
    print('O salario do funcionario apos o aumento e: {:.2f} Reai$'.format(leia_salario * 1.10))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)

#desafio 035
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