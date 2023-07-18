#leia um numero, mostre: seu dobro, triplo, raiz quadrada
num = float(input('Digite um numero: '))
num_dob = (num * 2)
num_tri = (num * 3)
num_raiz = (num ** (1/2))
print('O numero digitado foi: {}\nseu dobro é: {}\nseu triplo é: {}\nsua raiz quadrada é: {:.2f}'.format(num, num_dob, num_tri, num_raiz))

#outra forma de fazer:
'''
num_int = float(input('Digite um numero inteiro: '))
print('Passo define a razão de saida do programa!')
passo = float(input('Defina o passo: '))
num_int_tri = (num_int * 3)
num_int_dob = (num_int * 2)
num_int_raiz = num_int ** (1/2)
print('O dobro e: {} \nO triplo e: {} \nA raiz quadrada e: {}'.format(num_int_tri, num_int_dob, num_int_raiz))
'''
#o codigo acima, foi feito para que o usuario possa definir o passo, e assim, o programa possa ser mais dinamico