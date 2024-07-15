# aula 18; modulo 3; curso em video
#Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
# As listas são variáveis compostas que permitem armazenar vários valores em uma 
# mesma estrutura, acessíveis por chaves individuais

dados = list()
dados.append('Pedro')   
dados.append(25)
print(dados)
print(dados[0]) # mostra o primeiro elemento da lista
print(dados[1]) # mostra o segundo elemento da lista
pessoas = list()
pessoas.append(dados[:]) # cria uma cópia da lista dados
print(pessoas)
pessoas = [['Peds', 23], ['Maria', 19], ['João', 32]] # cria uma lista composta
print(pessoas[0][0]) # mostra o primeiro elemento da lista composta
print(pessoas[1][1]) # mostra o segundo elemento da lista composta
print(pessoas[2][0]) # mostra o terceiro elemento da lista composta
# navegando eplos componetes da lista composta, similar a matriz i j do c
print(pessoas[1]) # mostra o segundo elemento da lista composta

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
#galera.append(teste) # cria uma cópia da lista teste e vincula a lista galera
galera.append(teste[:]) # cria uma cópia da lista teste
teste[0] = 'Maria'
teste[1] = 22
print(galera)
print(teste)
galers = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galers[0])
for aux in galers:# para cada pessoa na lista galers
    print(f'{aux[0]} tem {aux[1]} anos de idade') # mostra o nome e a idade da pessoa

humano = list()
dado_humano = list()
for aux in range(0, 3):
    dado_humano.append(str(input('Nome: '))) # adiciona o nome na lista
    dado_humano.append(int(input('Idade: '))) # adiciona a idade na lista
    humano.append(dado_humano[:]) # cria uma cópia da lista dado_humano na lista humano
    dado_humano.clear() # limpa a lista dado_humano
print(humano)
maior_idade = menor_idade = 0
for aux in humano:
    if aux[1] >= 21:
        print(f'{aux[0]} é maior de idade')
        maior_idade += 1
    else:
        print(f'{aux[0]} é menor de idade')
        menor_idade += 1
print(f'Temos {maior_idade} maiores e {menor_idade} menores de idade')
