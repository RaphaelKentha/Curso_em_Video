#aula 16; modulo 3; curso em video
# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# docstrings para funções, argumentos opcionais para funções, escopo de variáveis e retorno de resultados
# de funções. Vamos ter também alguns exemplos práticos com funções em Python

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[3]) # mostra o elemento 3 da tupla
print(lanche[-2]) # mostra o penultimo elemento da tupla
print(lanche[1:3]) # mostra os elementos 1 e 2 da tupla
print(lanche[2:]) # mostra os elementos a partir do elemento 2

for comida in lanche: # in lanche é o mesmo que in range(0, len(lanche))
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for aux in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[aux]}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche): # enumerate mostra a posição e o elemento
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # sorted mostra a tupla em ordem alfabética

tupla_a = (2, 5, 4)
tupla_b = (5, 8, 1, 2)
tupla_c = tupla_a + tupla_b
print(tupla_c)
print(len(tupla_c))
print(tupla_c.count(5)) # quantas vezes aparece o número 5
print(tupla_c.index(8)) # em qual posição está o número 8
print(tupla_c.index(5, 1)) # em qual posição está o número 5 a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) # apaga a tupla inteira

# tuplas são imutáveis
# lanche[1] = 'Refrigerante' # não funciona

# para alterar uma tupla, é preciso transformá-la em lista
# lanche = list(lanche)
# lanche[1] = 'Refrigerante'

#desafio 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
from time import sleep

print('-='*35)
print('{:=^81}'.format('\33[30;42mNumeros por extenso\33[m'))
print('-='*35)

tupla20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero_teclado = input('Digite um número entre 0 e 20: ')
    if numero_teclado.isnumeric() == False: # se não for um número
        print('Você não digitou um número')
    else:
        aux = int(numero_teclado)
        if aux < 0 or aux > 20:
            print('Você digitou um número fora do intervalo')
        else:
            break
print('Processando...')
sleep(1)
print(f'Você digitou o número {tupla20[int(numero_teclado)]}') # mostra o número por extenso digitado pelo usuário
print('\033[1;30;41m}#{|\033[m' * 20)


#desafio 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) apenas os 5 primeiros colocados
# b) os últimos 4 colocados da tabela
# c) uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time da Chapecoense
print('-='*35)
print('{:=^81}'.format('\33[30;42mTabela do Brasileirão\33[m'))
print('-='*35)

tupla_brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Os times em ordem alfabética são:')
print('Processando...')
sleep(1)
print(sorted(tupla_brasileirao))
print('-='*35)
for aux in range(0, len(tupla_brasileirao)):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.15)
print('-='*35)
print('Processando...')
sleep(1)
print(f'Os 5 primeiros colocados são:')
for aux in range(0, 5):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.09)
print('-='*35)
print('Processando...')
sleep(1)
print(f'Os 4 últimos colocados são:')
for aux in range(16, 20):
    print(f'{aux+1}º {tupla_brasileirao[aux]}')
    sleep(0.09)
print('-='*35)
print('Processando...')
sleep(1)
print('Posição da Chapecoense:')
if 'Chapecoense' in tupla_brasileirao:
    print(f'Está na {tupla_brasileirao.index("Chapecoense")+1}ª posição')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random
print('-='*35)
print('{:=^81}'.format('\33[30;42mNúmeros aleatórios\33[m'))
print('-='*35)
sleep(0.3)

tupla_numeros_aleatorios = random.sample(range(0, 100), 5) # gera 5 números aleatórios entre 0 e 100
#ou pode ser:
#for aux in range(0, 5):
#    tupla_numeros_aleatorios[aux] = random.randint(0, 100)
sleep(0.1)
print(f'Os números sorteados foram: {tupla_numeros_aleatorios}')
sleep(0.1)
print(f'O maior número sorteado foi {max(tupla_numeros_aleatorios)}')
sleep(0.1)
print(f'O menor número sorteado foi {min(tupla_numeros_aleatorios)}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro valor 3
# c) quais foram os números pares
print('-='*35)
print('{:=^81}'.format('\33[30;42mNúmeros aleatórios\33[m'))
print('-='*35)

tupla_de_4 = ()
conta_9 = 0
posicao_3 = 0

print('Digite 4 números')
for aux in range(0, 4):
    tupla_de_4 += (int(input('Digite um número: ')),) # a vírgula é necessária para que o programa entenda que é uma tupla
    sleep(0.1)
    if tupla_de_4[aux] == 9:
        conta_9 += 1
    elif tupla_de_4[aux] == 3:
        posicao_3 = aux + 1
    if tupla_de_4[aux] % 2 == 0: # se o resto da divisão por 2 for 0
        print(f'{tupla_de_4[aux]} é par')
print(f'O número 9 apareceu {conta_9} vezes')
if posicao_3 == 0:
    print('O número 3 não apareceu')
else:
    print(f'O número 3 apareceu na posição {posicao_3}')
print(f'Você digitou os valores {tupla_de_4}')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 76
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
print('-='*35)
print('{:=^81}'.format('\33[30;42mListagem de preços\33[m'))
print('-='*35)

tupla_produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for aux in range(0, len(tupla_produtos), 2):
    sleep(0.17)
    print(f'{tupla_produtos[aux]:.<30}R$ {tupla_produtos[aux+1]:>7.2f}') # :.<30 alinha a esquerda com 30 caracteres e :>7.2f alinha a direita com 7 caracteres e 2 casas decimais
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 77
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais
print('-='*35)
print('{:=^81}'.format('\33[30;42mVogais em tupla\33[m'))
print('-='*35)

tupla_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for aux in range(0, len(tupla_palavras)):
    sleep(0.17)
    print(f'\nNa palavra {tupla_palavras[aux].upper()} temos ', end='') # end='' faz com que o print não pule linha
    for letra in tupla_palavras[aux]:
        if letra.lower() in 'aeiou': # se a letra for vogal
            sleep(0.09)
            print(letra, end=' ')


