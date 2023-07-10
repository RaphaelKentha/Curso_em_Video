#faca um programa que leia algo pelo teclado e mostre
#seu tipo primitivo e informacoes sobre a mesma

thinks = input('Digite algo: ')
print(type(thinks))
print('e numerico?', thinks.isalnum())
print('e alfanumerico?', thinks.isalpha())
print('e um numero? ', thinks.isnumeric())
print('so tem espacos?', thinks.isspace())
