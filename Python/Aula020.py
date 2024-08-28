# aula 20; modulo 3; curso em video
'''Nessa aula, vamos aprender o que são funções ou rotinas e 
como utilizar funções em Python. Funções são trechos de código 
que podem ser executados em momentos diferentes de nossos códigos 
em Python. Veja como funciona o comando def em Python e como utilizá-lo 
com parâmetros simples e múltiplos'''

def mostraLinha():
    print('-#' * 30)


mostraLinha() #mostra uma linha

def mensagem(msg): #função que mostra uma mensagem, msg é o parâmetro
    print('-#' * 30)
    print(msg)
    print('-#' * 30)


mensagem('\tSISTEMA DE ALUNOS') #mostra uma mensagem dada pelo usuário
mensagem('\tSISTEMA DE PROFESSORES')
mensagem('\tSISTEMA DE FUNCIONÁRIOS')

def soma(a, b): #função que soma dois números
    s = a + b
    print(s) #mostra a soma dos números

somar = soma(4, 5) #soma 4 e 5 = 9
#soma recebe dois parâmetros, 4 e 5
soma(a=2, b=3) #soma 2 e 3 = 5, definindo os parâmetros especificamente


def contador(*num): #função que conta os números
    print(num) #mostra os números
    #*num empacota os números em uma tupla, mesmo que não tenha parâmetros
    #previamente definidos

contador(2, 1, 7) #mostra os números 2, 1 e 7
contador(8, 0) #mostra os números 8 e 0


def dobra(lista): #função que dobra os números
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    return lista #retorna a lista com os números dobrados
#dado uma lista a funcao dobra percorrera a lista e dobrara os valores


valores = [6, 3, 9, 1, 0, 2] #lista de valores
print(valores) #mostra a lista valores
dobra(valores) #dobra os valores da lista

def soma(*valores): #função que soma os valores
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}') #mostra a soma dos valores
#funcao soma recebe uma quantidade de parametros indefinidos