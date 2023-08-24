#Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

tupla_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for aux in range(0, len(tupla_palavras)):
    print(f'\nNa palavra {tupla_palavras[aux].upper()} temos ', end = '')
    for aux2 in range(0, len(tupla_palavras[aux])):
        if tupla_palavras[aux][aux2] in 'aeiou':
            print(tupla_palavras[aux][aux2], end = ' ')

# meu codigo:
'''
from time import sleep

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
print('\033[1;30;41m}#{|\033[m' * 20)
'''