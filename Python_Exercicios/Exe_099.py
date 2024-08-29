#desafio 99
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles
# é o maior.

def maior_valor(*numeros):
    print('-=' *26)
    print('Analisando os valores passados...')
    if numeros == ():
        print('Nenhum valor foi informado.')
    else:
        for aux in numeros:
            print(aux, end=' ')
        print(f'Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior valor informado foi {max(numeros)}')

maior_valor(2, 9, 4, 5, 7, 1)
maior_valor(4, 7, 0)
maior_valor(1, 2)
maior_valor(6)
maior_valor()
