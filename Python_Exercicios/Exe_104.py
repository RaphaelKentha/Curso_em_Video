#desafio 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico


def leia_int(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print('\33[0;30;41mERRO! Digite um número inteiro válido.\33[m')

print(leia_int('Digite um número: '))
