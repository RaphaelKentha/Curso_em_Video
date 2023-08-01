# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os 
# N primeiros elementos de uma Sequência de Fibonacci
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8


fibonacci_numero = int(input('Digite um número para saber sua sequência de Fibonacci: '))
f1 = 0
f2 = 1
count = 0
print('{} - {}'.format(f1, f2), end=' - ')

while count < fibonacci_numero:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    count += 1
    print(f3, end=' - ')
print('FIM')

# meu codigo:
'''
from time import sleep
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mSequência de Fibonacci\33[m'))
print('#=' * 35)
numero_de_fibo = int(input('Digite o numero de elementos da sequência de Fibonacci: '))
print('Aguarde...')
sleep(1)
fibo2 = 1
fibo3 = 1
fibonacci = 0
aux_fibo = 3
if numero_de_fibo == 1:
    print('A sequência de Fibonacci é: 0')
elif numero_de_fibo == 2:
    print('A sequência de Fibonacci é: 0 -> 1')
elif numero_de_fibo == 3:
    print('A sequência de Fibonacci é: 0 -> 1 -> 1', end=' -> ')
elif numero_de_fibo > 3:
    print('A sequência de Fibonacci é: 0 -> 1 -> 1', end=' -> ')
    while aux_fibo != numero_de_fibo:
        if numero_de_fibo > 2:
            fibonacci = fibo2 + fibo3
            fibo2 = fibo3
            fibo3 = fibonacci
            print(fibonacci, end=' -> ')
            aux_fibo += 1
else:
    print('O numero digitado é invalido')
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)
'''	