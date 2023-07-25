# Aula 12; modulo 2; curso em video
# |Condições Aninhadas| # if elif else
# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os
# comandos if.. elif.. else em programas Python.

nome = input('Qual é o seu nome? ').strip().capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')

#desafio 36
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será
# negado.
import time
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mEmpréstimo Bancário\33[m')
print('=$'*40)
print('Para realizar o empréstimo, precisamos de algumas informações: ')
valor_casa = float(input('Qual o valor da casa? R$: '))
print('Aguarde...')
sleep(1)
valor_salario = float(input('Qual o valor do seu salário? R$: '))
print('Aguarde...')
sleep(1)
finaceamento_anos = int(input('Em quantos anos você pretende pagar? ')) #adotando que o tempo maximo de financiamento é de 30 anos
print('Aguarde...')
sleep(1)
print('Calculando...')
sleep(3)
valor_da_prestacao = valor_casa / (finaceamento_anos * 12)
if valor_da_prestacao <= (valor_salario * 0.3) and finaceamento_anos <= 30 and valor_da_prestacao > 0 and valor_casa > 0 and valor_salario > 0:
    print('\33[30;42mParabéns, seu empréstimo foi aprovado!\33[m')
    print('O valor da prestação será de R$ {:.2f}'.format(valor_da_prestacao))
else:
    print('\33[0;30;41mInfelizmente seu empréstimo não foi aprovado.\33[m')
    print('O valor da prestação seria de R$ {:.2f}'.format(valor_da_prestacao))
print('=$'*40)

#desafio 37
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('=$'*40)
print('\t\t\t\33[30;42mConversor de Bases Numéricas\33[m')
print('=$'*40)
numero = int(input('Digite um número inteiro: '))
opcao_de_conversao = int(input('Escolha uma das opções abaixo: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha: '))
print('Aguarde...')
sleep(1)
if opcao_de_conversao == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao_de_conversao == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao_de_conversao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
print('=$'*40)

#desafio 38
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela
# uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
print('=$'*40)
print('\t\t\t\33[30;42mComparador de Números\33[m')
print('=$'*40)
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
print('Aguarde...')
sleep(1)
if numero1 > numero2:
    print('O primeiro número é maior que o segundo.')
elif numero1 < numero2:
    print('O segundo número é maior que o primeiro.')
else:
    print('Os dois números são iguais.')
print('=$'*40)

#desafio 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
# sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se
# alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
from datetime import date
print('=$'*40)
print('\t\t\t\33[30;42mAlistamento Militar\33[m')
print('=$'*40)
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
print('Aguarde...')
sleep(1)
ano_atual = date.today().year #ano atual
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você ainda não tem 18 anos, faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você tem 18 anos, está na hora de se alistar.')
else:
    print('Você já passou da idade de se alistar, passaram {} anos.'.format(idade - 18))
print('=$'*40)

#desafio 40
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print('=$'*40)
print('\t\t\t\33[30;42mMédia Escolar\33[m')
print('=$'*40)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('Aguarde...')
sleep(1)
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi {:.1f}, você está \33[0;30;41mREPROVADO\33[m.'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi {:.1f}, você está de \33[0;30;43mRECUPERAÇÃO\33[m.'.format(media))
else:
    print('Sua média foi {:.1f}, você está \33[0;30;42mAPROVADO\33[m.'.format(media))
print('=$'*40)

#desafio 41
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
print('=$'*40)
print('\t\t\t\33[30;42mCategoria de Natação\33[m')
print('=$'*40)
nome_do_atleta = input('Digite o nome do atleta: ').strip().capitalize()
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year #ano atual
idade_do_atleta = ano_atual - ano_nascimento
if idade_do_atleta <= 9:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;42mMIRIM\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 9 and idade_do_atleta <= 14:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;43mINFANTIL\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 14 and idade_do_atleta <= 19:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;44mJUNIOR\33[m.'.format(nome_do_atleta, idade_do_atleta))
elif idade_do_atleta > 19 and idade_do_atleta <= 25:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;45mSÊNIOR\33[m.'.format(nome_do_atleta, idade_do_atleta))
else:
    print('O atleta {} tem {} anos e está na categoria \33[0;30;46mMASTER\33[m.'.format(nome_do_atleta, idade_do_atleta))
print('=$'*40)

#desafio 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
print('=$'*40)
print('\t\t\t\33[30;42mAnalisador de Triângulos\33[m')
print('=$'*40)
lado_a = float(input('Digite o comprimento do lado A: '))
lado_b = float(input('Digite o comprimento do lado B: '))
lado_c = float(input('Digite o comprimento do lado C: '))
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
#desafio 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print('=$'*40)
print('\t\t\t\33[30;42mCalculadora de IMC\33[m')
print('=$'*40)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2) #altura elevado ao quadrado
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está \33[0;30;41mABAIXO DO PESO\33[m.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, você está no \33[0;30;42mPESO IDEAL\33[m.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}, você está com \33[0;30;43mSOBREPESO\33[m.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}, você está com \33[0;30;44mOBESIDADE\33[m.'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com \33[0;30;45mOBESIDADE MÓRBIDA\33[m.'.format(imc))
print('=$'*40)

#desafio 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o
# seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('=$'*40)
print('\t\t\t\33[30;42mCalculadora de Preços\33[m')
print('=$'*40)
numero_de_parcelas = 0
preco_do_produto = float(input('Digite o preço do produto: R$ '))
tipo_de_pagamento = int(input('Digite o tipo de pagamento: \n1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão\nEscolha: '))
if tipo_de_pagamento == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco_do_produto * 0.9))
elif tipo_de_pagamento == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco_do_produto * 0.95))
elif tipo_de_pagamento == 3:
    print('O valor a ser pago é de R$ {:.2f} em 2X'.format(preco_do_produto / 2))
elif tipo_de_pagamento == 4:
    numero_de_parcelas = int(input('Digite o número de parcelas: '))
    print('O valor a ser pago é de R$ {:.2f} em {}X'.format(((preco_do_produto * 1.2) / numero_de_parcelas) , numero_de_parcelas))
print('=$'*40)

#desafio 45
# Crie um programa que faça o computador jogar Jokenpô com você.
import random

print('=$'*40)
print('\t\t\t\33[30;42mJokenpô\33[m')
print('=$'*40)
print('Vamos jogar Jokenpô?')
print('Escolha uma das opções abaixo: ')
print('1 - Pedra\n2 - Papel\n3 - Tesoura')
pedra = 1
papel = 2
tesoura = 3
lista = [pedra, papel, tesoura]
jogada_do_computador = random.choice(lista)
jogada_do_jogador = int(input('Digite sua jogada: '))
print('Jon...')
sleep(1)
print('Ken...')
sleep(1)
print('Pô!!!')
sleep(1)
if jogada_do_computador == 1:
    print('O computador escolheu Pedra!')
elif jogada_do_computador == 2:
    print('O computador escolheu Papel!')
else:
    print('O computador escolheu Tesoura!')

if jogada_do_jogador == 1:
    print('Você escolheu Pedra!')
elif jogada_do_jogador == 2:
    print('Você escolheu Papel!')
else:
    print('Você escolheu Tesoura!')

if jogada_do_computador == jogada_do_jogador:
    print('Empate!')
elif jogada_do_computador == 1 and jogada_do_jogador == 2:
    print('Você ganhou!')
elif jogada_do_computador == 1 and jogada_do_jogador == 3:
    print('Você perdeu!')
elif jogada_do_computador == 2 and jogada_do_jogador == 1:
    print('Você perdeu!')
elif jogada_do_computador == 2 and jogada_do_jogador == 3:
    print('Você ganhou!')
elif jogada_do_computador == 3 and jogada_do_jogador == 1:
    print('Você ganhou!')
elif jogada_do_computador == 3 and jogada_do_jogador == 2:
    print('Você perdeu!')
else:
    print('Jogada inválida!')
