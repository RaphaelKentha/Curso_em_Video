# aula 22; modulo 3; curso em video
'''Nessa aula, vamos continuar nossos estudos de funções em Python, 
aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. 
Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais 
a modularização em grandes projetos em Python.'''

#daddo a utlilização de modulos, podemos criar um modulo para cada função
#dessa forma, podemos reutilizar o código em outros projetos

import Aula022_modulos
#importando o modulo Aula022_modulos, no caso o fatotial

#programa principal
consulta = int(input('Digite um número para calcular o fatorial: '))
print(f'O fatorial de {consulta} é {Aula022_modulos.fatorial(consulta)}')