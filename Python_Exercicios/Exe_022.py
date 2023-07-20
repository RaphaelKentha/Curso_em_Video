#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome_completo = input('Digite seu nome completo: ')
print('Seu nome em maiusculas é: {}'.format(nome_completo.upper()))
print('Seu nome em minusculas é: {}'.format(nome_completo.lower()))
quantidade_de_letras_nome = len(nome_completo) - nome_completo.count(' ')
print('Seu nome tem {} letras'.format(quantidade_de_letras_nome))
print('Seu primeiro nome é: {}'.format(nome_completo.split()[0]))
#codigo acima e mais objetivo
'''
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
'''