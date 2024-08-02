# aula 19; modulo 3; curso em video
'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar
dicionários em Python. Os dicionários são variáveis compostas que 
permitem armazenar vários valores em uma mesma estrutura, acessíveis
por chaves literais'''

dicionario_dados = dict()
#inicia o dicionário
dicionario_dados = {'nome': 'Pedro', 'idade': 25}
#temos como chave o nome e a idade que sao os "novos indices"
print(dicionario_dados) # mostra o dicionário, pedro e 25
dicionario_dados['sexo'] = 'M' # adiciona o sexo ao dicionário
print(dicionario_dados) # mostra o dicionário, pedro, 25 e M
del dicionario_dados['idade'] # deleta a idade do dicionário
print(dicionario_dados) # mostra o dicionário, pedro e M
dados_filme1 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
# cria um dicionário com o título, ano e diretor do filme
print(dados_filme1.values()) # mostra os valores do dicionário, os valores são os elementos do dicionário
print(dados_filme1.keys()) # mostra as chaves do dicionário, as chaves são os indices do dicionário
print(dados_filme1.items()) # mostra os itens do dicionário, 
# os itens são os elementos do dicionário
for key, value in dados_filme1.items():
    print(f'O {key} é {value}')
#percorre o dicionário e mostra a chave e o valor

dados_filme2 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
dados_filme3 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
#lista de dicionários
locadora = list()
locadora.append(dados_filme1) # adiciona o dicionário dados_filme na lista locadora
print(locadora) # mostra a lista locadora
locadora.append(dados_filme2) # adiciona o dicionário dados_filme2 na lista locadora
locadora.append(dados_filme3) # adiciona o dicionário dados_filme3 na lista locadora
print(locadora[1]) # mostra a lista locadora


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # mostra o dicionário pessoas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') 
# mostra o nome e a idade da pessoa formatado
pessoas['peso'] = 98.5 # adiciona o peso ao dicionário
for keys, values in pessoas.items():
    print(f'{keys} = {values}')
# percorre o dicionário e mostra a chave e o valor
# no dicionario usamos o .items() para percorrer o dicionário

estados_brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estados_brasil.append(estado1)
estados_brasil.append(estado2)
print(estados_brasil)

estadoN = dict()
for aux in range(0, 2):
    estadoN['uf'] = str(input('Unidade Federativa: '))
    estadoN['sigla'] = str(input('Sigla do Estado: '))
    estados_brasil.append(estadoN.copy())
print(estados_brasil)
# o laco acima usa o dict estadoN para adicionar elementos
# ao dicionário estados_brasil, o .copy() é usado para copiar

for aux in estados_brasil:
    for keys, values in aux.items():
        print(f'O campo {keys} tem valor {values}')
#o primeiro for percorre a lista estados_brasil
#o segundo for percorre o dicionário que está na lista