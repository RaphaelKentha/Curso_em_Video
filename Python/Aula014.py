#aula 14; modulo 2; curso em video
# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python
#Por exemplo:

cte = 1 
while cte != 10:
    print(cte)
    cte += 1
print('Acabou')

condicao_var = 'S'
while  condicao_var == 'S':
    numero = int(input('Digite um valor: '))
    condicao_var = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

numero_teste = 1
par = 0
impar = 0
while numero_teste != 0:
    numero_teste = int(input('Digite um numero: '))
    if numero_teste != 0:
        if numero_teste % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))

#desafio 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.
from time import sleep

print('=#' * 35)
print('{:=^81}'.format('\33[30;42mValidação de dados\33[m'))
print('=#' * 35)
validacao = 0
while validacao == 0:
    sexo_user = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo_user =='M' or sexo_user == 'F':
        validacao = 1
        print('Aguarde...')
        sleep(0.5)
        if sexo_user == 'M':
            print('Você é do sexo Masculino')
        else:
            print('Você é do sexo Feminino')
print('Fim do programa')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 58
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
# necessários para vencer.
import random
validacao_jogo = False
contadao_de_tentativas = 0
while validacao_jogo == False:
    numero_aletorio_pc = random.randint(0, 10)
    numero_do_jogador = int(input('Digite um numero de 0 a 10: '))
    if numero_do_jogador == numero_aletorio_pc:
        validacao_jogo = True
        print('Computador pensando...')
        sleep(0.5)
        print('Você acertou!')
        print('O numero que o computador escolheu foi {}'.format(numero_aletorio_pc))
        print('O numero que você escolheu foi {}'.format(numero_do_jogador))
    else:
        print('Computador pensando...')
        sleep(0.5)
        print('Você errou!')
        print('O numero que o computador escolheu foi {}'.format(numero_aletorio_pc))
        print('O numero que você escolheu foi {}'.format(numero_do_jogador))
    contadao_de_tentativas += 1
print('Você precisou de {} tentativas para acertar!'.format(contadao_de_tentativas))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 59
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mCalculadora\33[m'))
print('=#' * 35)
validacao_calculadora = 0

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
print('Aguarde...')
sleep(0.5)
print('O que você deseja fazer com os numeros {} e {}?'.format(numero_1, numero_2))
print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
opcao = int(input('Digite a opção desejada: '))
while validacao_calculadora == 0:
    if opcao == 1:
        print('Somando...')
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(numero_1, numero_2, numero_1 + numero_2))
        validacao_calculadora = 1
    elif opcao == 2:
        print('Multiplicando...')
        sleep(0.5)
        print('A multiplicação entre {} e {} é {}'.format(numero_1, numero_2, numero_1 * numero_2))
        validacao_calculadora = 1
    elif opcao == 3:
        print('Verificando...')
        sleep(0.5)
        if numero_1 > numero_2:
            print('O numero {} é maior que {}'.format(numero_1, numero_2))
            validacao_calculadora = 1
        elif numero_2 > numero_1:
            print('O numero {} é maior que {}'.format(numero_2, numero_1))
            validacao_calculadora = 1
        else:
            print('Os numeros são iguais')
            validacao_calculadora = 1
    elif opcao == 4:
        print('Reiniciando...')
        sleep(0.5)
        numero_1 = int(input('Digite o primeiro numero: '))
        numero_2 = int(input('Digite o segundo numero: '))
        print('Aguarde...')
        sleep(0.5)
        print('O que você deseja fazer com os numeros {} e {}?'.format(numero_1, numero_2))
        print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input('Digite a opção desejada: '))
    elif opcao == 5:
        print('Saindo...')
        sleep(0.5)
        validacao_calculadora = 1
print('\033[1;30;41m}#{|\033[m' * 20)
# codigo abaixo é o mesmo do de cima usando lista
lita_numero = []
elemnto1 = int(input('Digite o primeiro numero: '))
lita_numero.append(elemnto1)
elemnto2 = int(input('Digite o segundo numero: '))
lita_numero.append(elemnto2)
validacao_lista = False
while validacao_lista == False:
    print( 'Escolha: [1] - soma, [2] - multiplicação, [3] - maior, [4] - novos numeros, [5] - sair do programa')
    opcao_lista = int(input('Digite a opção desejada: '))
    if opcao_lista == 1:
        print('Somando...')
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(elemnto1, elemnto2, sum(lita_numero)))
        validacao_lista = True
    elif opcao_lista == 2:
        print('Multiplicando...')
        sleep(0.5)
        print('A multiplicação entre {} e {} é {}'.format(elemnto1, elemnto2, elemnto1 * elemnto2))
        validacao_lista = True
    elif opcao_lista == 3:
        print('Verificando...')
        sleep(0.5)
        if elemnto1 == elemnto2:
            print('Os numeros são iguais')
            validacao_lista = True
        else:
            print('O maior numero entre {} e {} é {}'.format(elemnto1, elemnto2, max(lita_numero)))
    elif opcao_lista == 4:
        print('Reiniciando...')
        sleep(0.5)
        elemnto1 = int(input('Digite o primeiro numero: '))
        lita_numero.append(elemnto1)
        elemnto2 = int(input('Digite o segundo numero: '))
        lita_numero.append(elemnto2)
        print('Aguarde...')
        sleep(0.5)
        print('O que você deseja fazer com os numeros {} e {}?'.format(elemnto1, elemnto2))
        print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao_lista = int(input('Digite a opção desejada: '))
    elif opcao_lista == 5:
        print('Saindo...')
        sleep(0.5)
        validacao_lista = True

#desafio 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
import math
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

#desafio 61
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('#=' * 35)
print('{:=^81}'.format('\33[30;42m10 Termos da PA\33[m'))
print('#=' * 35)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
print('Aguarde...')
sleep(1)
aux_while = 0
while aux_while != 10:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao_pa
    aux_while += 1
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 62
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mX Termos da PA\33[m'))
print('#=' * 35)
print('A configuração padrão é de 10 termos')
alteracao_n_termos = int(input('Deseja alterar a quantidade de termos? [1] - Sim, [2] - Não: '))
if alteracao_n_termos == 1:
    n_termos = int(input('Digite a quantidade de termos: '))    
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao_pa = int(input('Digite a razão da PA: '))
    print('Aguarde...')
    sleep(1)
    aux_while = 0
    while aux_while != n_termos:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao_pa
        aux_while += 1
else:
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao_pa = int(input('Digite a razão da PA: '))
    print('Aguarde...')
    sleep(1)
    aux_while = 0
    while aux_while != 10:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao_pa
        aux_while += 1
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 63
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros 
# elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mSequência de Fibonacci\33[m'))
print('#=' * 35)
numero_de_fibo = int(input('Digite o numero de elementos da sequência de Fibonacci: '))
print('Aguarde...')
sleep(1)
fibo2 = 1
fibo3 = 1
fibonacci = 0
aux_fibo = 3
if numero_de_fibo == 1:
    print('A sequência de Fibonacci é: 0')
elif numero_de_fibo == 2:
    print('A sequência de Fibonacci é: 0 -> 1')
elif numero_de_fibo == 3:
    print('A sequência de Fibonacci é: 0 -> 1 -> 1', end=' -> ')
elif numero_de_fibo > 3:
    print('A sequência de Fibonacci é: 0 -> 1 -> 1', end=' -> ')
    while aux_fibo != numero_de_fibo:
        if numero_de_fibo > 2:
            fibonacci = fibo2 + fibo3
            fibo2 = fibo3
            fibo3 = fibonacci
            print(fibonacci, end=' -> ')
            aux_fibo += 1
else:
    print('O numero digitado é invalido')
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 64
# Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles
#  (desconsiderando o flag).
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mSoma de números inteiros\33[m'))
print('#=' * 35)
cont_numero = 0
soma_numero = 0
valid_999 = False
while valid_999 == False:
    num_inteiro = int(input('Digite o {} numero: '.format(cont_numero + 1)))
    if num_inteiro == 999:
        valid_999 = True
    else:
        cont_numero += 1
        soma_numero += num_inteiro
print('Aguarde...')
sleep(1)
print('A soma dos {} numeros digitados é {}'.format(cont_numero, soma_numero))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 65
# Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mMédia, maior e menor valor\33[m'))
print('#=' * 35)
lista_numeros65 = []
aux65 = False
while aux65 == False:
    lista_numeros65.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        aux65 = True
print('Aguarde...')
sleep(1)
print('A média dos numeros digitados é {}'.format(sum(lista_numeros65) / len(lista_numeros65)))
print('O maior numero digitado foi {}'.format(max(lista_numeros65)))
print('O menor numero digitado foi {}'.format(min(lista_numeros65)))
print('\033[1;30;41m}#{|\033[m' * 20)
