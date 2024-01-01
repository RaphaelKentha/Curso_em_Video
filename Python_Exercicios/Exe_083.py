# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

count_open_parenteses = 0
count_close_parenteses = 0
expressao_matematica = str(input('Digite uma expressão matemática: '))

for aux in expressao_matematica:
    if aux == '(':
        count_open_parenteses += 1
    elif aux == ')':
        count_close_parenteses += 1
if count_open_parenteses == count_close_parenteses:
    print('A expressão está válida!')
else:
    print('A expressão está inválida!')

# meu codigo:
'''
print('-='*35)
print('{:=^81}'.format('\33[30;42mValidando expressões matemáticas\33[m'))
print('-='*35)

expressao_matematica = str(input('Digite uma expressão matemática: '))
count_open_parenteses = 0
count_close_parenteses = 0

for aux in range(0, len(expressao_matematica)):
    if expressao_matematica[aux] == '(':
        count_open_parenteses += 1
    elif expressao_matematica[aux] == ')':
        count_close_parenteses += 1
if count_open_parenteses == count_close_parenteses:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')
print('\033[1;30;41m}#{|\033[m' * 20)
'''
