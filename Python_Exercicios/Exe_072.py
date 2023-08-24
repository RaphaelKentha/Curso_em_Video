# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem 
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
# (entre 0 e 20) e mostrá-lo por extenso

tupla10 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
tupla20 = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 > num > 20:
        print('Tente novamente. ', end='')
    elif 0 <= num <= 10:
        print(f'Você digitou o número {tupla10[num]}')
        break
    elif 11 <= num <= 20:
        print(f'Você digitou o número {tupla20[num-11]}')
        break
    
#meu codigo:
'''
from time import sleep

print('-='*35)
print('{:=^81}'.format('\33[30;42mNumeros por extenso\33[m'))
print('-='*35)

tupla20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero_teclado = input('Digite um número entre 0 e 20: ')
    if numero_teclado.isnumeric() == False: # se não for um número
        print('Você não digitou um número')
    else:
        aux = int(numero_teclado)
        if aux < 0 or aux > 20:
            print('Você digitou um número fora do intervalo')
        else:
            break
print('Processando...')
sleep(1)
print(f'Você digitou o número {tupla20[int(numero_teclado)]}') # mostra o número por extenso digitado pelo usuário
print('\033[1;30;41m}#{|\033[m' * 20)
'''