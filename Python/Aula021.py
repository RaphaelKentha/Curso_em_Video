# aula 21; modulo 3; curso em video
'''Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais dinamismo
em funções Python, escopo de variáveis e retorno de resultados'''

#interactive help
#help() #mostra o manual da função
help(print) #mostra o manual da função print
print(input.__doc__) #outra forma de mostrar o manual da função

#docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
# as docstrings são utilizadas para documentar funções 
# logo após a definição da função
help(contador) #mostra o manual da função contador

#parametros opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    :obs: a função somar() é opcional, caso não seja passado nenhum valor
    :dado que os valores, = a zero, tonar-se-ão opcionais
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5) #soma 3, 2 e 5 = 10
somar(8, 4) #soma 8 e 4 = 12, sendo o valor de c = 0, pois ele é opcional

#escopo de variáveis
def teste():
    global n #n é uma variável global
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
# x e uma variavel local, ou seja, ela so existe dentro da funcao teste
# n e uma variavel global, ou seja, ela existe em todo o programa
# caso a funcao teste tenha um x, e o programa principal tenha um x global
# podemos forcar a funcao teste a usar o x global, atraves do comando global

#retorno de resultados
def somar_com_retorno(a=0, b=0, c=0):
    s = a + b + c
    return s
#funcao que retorna um valor
r1 = somar_com_retorno(3, 2, 5) #soma 3, 2 e 5 = 10
r2 = somar_com_retorno(2, 2) #soma 2 e 2 = 4, c = 0
r3 = somar_com_retorno(6) #soma 6, b e c = 0
print(f'Os resultados foram {r1}, {r2} e {r3}') #mostra os resultados