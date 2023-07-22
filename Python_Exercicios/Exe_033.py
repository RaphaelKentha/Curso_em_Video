# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o terceiro numero: '))
if numero_1 > numero_2 and numero_1 > numero_3:
    print('O maior numero e: {}'.format(numero_1))
elif numero_2 > numero_1 and numero_2 > numero_3:
    print('O maior numero e: {}'.format(numero_2))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print('O maior numero e: {}'.format(numero_3))

if numero_1 < numero_2 and numero_1 < numero_3:
    print('O menor numero e: {}'.format(numero_1))
elif numero_2 < numero_1 and numero_2 < numero_3:
    print('O menor numero e: {}'.format(numero_2))
elif numero_3 < numero_1 and numero_3 < numero_2:
    print('O menor numero e: {}'.format(numero_3))
print('Fim do programa')

# Meu codigo abaixo:
'''
# Leia tres numeros e mostre qual e o maior e qual e o menor
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))
lista_numeros = [numero1, numero2, numero3]
print('O maior numero e: {}'.format(max(lista_numeros)))
print('O menor numero e: {}'.format(min(lista_numeros)))
print('#' * 50)
if numero1 > numero2 and numero1 > numero3:
    print('O maior numero e: {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O maior numero e: {}'.format(numero2))
else:
    print('O maior numero e: {}'.format(numero3))
if numero1 < numero2 and numero1 < numero3:
    print('O menor numero e: {}'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('O menor numero e: {}'.format(numero2))
else:
    print('O menor numero e: {}'.format(numero3))
print('Fim do programa')
print('#' * 50)
'''