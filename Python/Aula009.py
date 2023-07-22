# Aula 9; modulo 1; curso em video
#   |Tratamento de texto|   #
# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são 
# o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), 
# capitalize(), title(), strip(), junção com join().
import random

frase = 'Curso em Video Python'
frase2 = '   Aprenda Python com o Curso em Video    '
# A contagem de elementos de uma string começa em 0, logo 'frase':
# |C|u|r|s|o| |e|m| |V|i|d|e|o| |P|y|t|h|o|n|
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20| <- indices
print(frase[20]) # retorna 'n' que é o elemento de indice 20
print(frase[0:]) # retorna 'Curso em Video Python' que é o elemento de indice 0 até o final
print(frase[0:13:2]) # retorna 'CsoeVdo' que é o elemento de indice 0 até 13 pulando de 2 em 2
print(frase[::2]) # retorna 'CsoeVdoPto' que é o elemento de indice 0 até o final pulando de 2 em 2
print(frase.count('o')) # retorna 3 que é a quantidade de vezes que o elemento 'o' aparece na string
print(frase.upper().count('O')) # retorna 3 que é a quantidade de vezes que o elemento 'O'(pois foi utilizado a .upper) aparece na string
print(frase.upper()) # retorna 'CURSO EM VIDEO PYTHON' que é a string em maiusculo
print(frase.lower()) # retorna 'curso em video python' que é a string em minusculo
print(len(frase)) # retorna 21 que é a quantidade de elementos da string
print(frase.replace('Python', 'Android')) # retorna 'Curso em Video Android' que é a string com o elemento 'Python' substituido por 'Android'
print(len(frase2)) # retorna 38 que é a quantidade de elementos da string
print(len(frase2.strip())) # retorna 35 que é a quantidade de elementos da string sem os espaços do inicio e do fim
print('Python' in frase) # retorna True que é a resposta para a pergunta 'Python' esta em 'frase'?
print(frase.find('Video')) # retorna 9 que é o indice do primeiro elemento da string 'Video' em 'frase'
print(frase.find('video')) # retorna -1 que é o indice do primeiro elemento da string 'video' em 'frase', como nao existe, retorna -1
print(frase.lower().find('video')) # retorna 9 que é o indice do primeiro elemento da string 'video' em 'frase' em minusculo
frase_dividida = frase.split() # retorna ['Curso', 'em', 'Video', 'Python'] que é a string dividida em uma lista
print(frase_dividida[0]) # retorna 'Curso' que é o primeiro elemento da lista
print(frase_dividida[0][2]) # retorna 'r' que é o elemento de indice 2 do primeiro elemento da lista
print('-'.join(frase_dividida)) # retorna 'Curso-em-Video-Python' que é a lista unida em uma string separada por '-'
print('-'.join(frase_dividida).lower()) # retorna 'curso-em-video-python' que é a lista unida em uma string separada por '-' e em minusculo
print('-'.join(frase_dividida).upper()) # retorna 'CURSO-EM-VIDEO-PYTHON' que é a lista unida em uma string separada por '-' e em maiusculo
random.shuffle(frase_dividida) # embaralha a lista
print(frase_dividida) # retorna ['Video', 'Curso', 'Python', 'em'] que é a lista embaralhada
print('''
 Aula 9; modulo 1; curso em video
                                       |Tratamento de texto|
 Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são 
o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().''')
# Utilizando 3 aspas simples ou duplas, é possivel escrever um texto com quebra de linha

print('#' * 125)
#desafio 022
# leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras em maiusculas
# o nome com todas as letras em minusculas
# numero de letras do nome, retirando os espacos
# e o numero de letras do primeiro nome
nome_completo = str(input('Digite seu nome completo: ')).strip() # remove os espaços do inicio e do fim
print('Seu noma completo: {}'.format(nome_completo.upper()))
print('#' * 50)
print('Seu noma completo: {}'.format(nome_completo.lower())) 
print('#' * 50)
nome_completo_numero_de_letras = len(nome_completo) - nome_completo.count(' ') # conta a quantidade de letras do nome completo sem os espaços
nome_completo_listagem = nome_completo.split() # divide o nome completo em uma lista
len(nome_completo_listagem[0]) # conta a quantidade de letras do primeiro elemento da lista
if len(nome_completo_listagem[0]) == 1:
    print('Seu primeiro nome: {} e tem {} letra'.format(nome_completo_listagem[0], len(nome_completo_listagem[0])))
else:
    print('Seu primeiro nome: {} e tem {} letras'.format(nome_completo_listagem[0], len(nome_completo_listagem[0])))
if nome_completo_numero_de_letras == 1:
    print('Seu nome completo: {} e tem {} letra'.format(nome_completo, nome_completo_numero_de_letras))
else:
    print('Seu nome completo: {} e tem {} letras'.format(nome_completo, nome_completo_numero_de_letras))
print('#' * 50)

#desafio 023
# leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
var_numero_inteiro = int(input('Digite um numero de 0 a 9999: '))
var_numero_string = str(var_numero_inteiro).split() # divide o numero em uma lista
for i in range(0, len(var_numero_string[0])): # para cada elemento da lista
    print('{} é o {} elemento da lista'.format(var_numero_string[0][i], i+1)) # imprime o elemento
# pesquisar como incluir o zero a esquerda, supondo que seja um numero 0989
# pois o mesmo sera convertido para 989
print('#' * 50)

#desafio 024
# crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome 'SANTO'
receba_nome_cidade = input('Digite o nome de uma cidade: ').strip() # remove os espaços do inicio e do fim
print('SANTO' in receba_nome_cidade.upper().split()[0]) # verifica se o primeiro elemento da lista em maiusculo contem 'SANTO'
if ('SANTO' in receba_nome_cidade.upper().split()[0]) == True:
    print('A cidade: {} comeca com o nome SANTO'.format(receba_nome_cidade.upper()))
else:
    print('A cidade: {} nao comeca com o nome SANTO'.format(receba_nome_cidade.upper()))
print('#' * 50)

#desafio 025
# crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
leia_nome_pessoa = input('Digite o nome de uma pessoa: ').strip() # remove os espaços do inicio e do fim
print('SILVA' in leia_nome_pessoa.upper().split()) # verifica se a lista em maiusculo contem 'SILVA'
if ('SILVA' in leia_nome_pessoa.upper().split()) == True:
    print('O nome: {} tem SILVA'.format(leia_nome_pessoa.upper()))
else:
    print('O nome: {} nao tem SILVA'.format(leia_nome_pessoa.upper()))
print('#' * 50)

#desafio 026
# leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'A'
# em que posicao ela aparece a primeira vez
# em que posicao ela aparece a ultima vez
leia_frase = input('Digite uma frase: ').strip() # remove os espaços do inicio e do fim

if len(leia_frase) == 1:  # conta a quantidade de vezes que a letra 'A' aparece na frase
    print('A letra "A" aparece {} vez na frase'.format(leia_frase.count('A')))
else:
    print('A letra "A" aparece {} vezes na frase'.format(leia_frase.count('A')))
print('A letra "A" aparece pela primeira vez na posicao {}'.format(leia_frase.find('A')+1)) # mostra a posicao da primeira vez que a letra 'A' aparece
print('A letra "A" aparece pela ultima vez na posicao {}'.format(leia_frase.rfind('A')+1)) # mostra a posicao da ultima vez que a letra 'A' aparece
#nota: o +1 foi utilizado para que a posicao seja mostrada a partir de 1 e nao de 0
#nota: o rfind() retorna a posicao da ultima vez que a letra 'A' aparece, pois comeca a contagem da direita(rigth)
print('#' * 50)

#desafio 027
# faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
# ultimo nome separadamente
nome_completo2 = input('Digite seu nome completo: ').strip() # remove os espaços do inicio e do fim
if len(nome_completo2.split()) == 0: # verifica se o nome tem apenas um elemento
    print('Voce nao digitou um nome')
elif len(nome_completo2.split()) == 1: # verifica se o nome tem apenas um elemento
    print('Voce digitou apenas um nome: {}'.format(nome_completo2.split()[0]))
else:
    print('Seu primeiro nome: {}\nSeu ultimo nome: {}'.format(nome_completo2.split()[0], nome_completo2.split()[-1]))