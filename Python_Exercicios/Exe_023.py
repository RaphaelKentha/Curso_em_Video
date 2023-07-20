#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
print('#' * 50)

#o mesmo codigo com laco:
'''
var_numero_inteiro = int(input('Digite um numero de 0 a 9999: '))
var_numero_string = str(var_numero_inteiro).split() # divide o numero em uma lista
for i in range(0, len(var_numero_string[0])): # para cada elemento da lista
    print('{} é o {} elemento da lista'.format(var_numero_string[0][i], i+1)) # imprime o elemento
# pesquisar como incluir o zero a esquerda, supondo que seja um numero 0989
# pois o mesmo sera convertido para 989
'''