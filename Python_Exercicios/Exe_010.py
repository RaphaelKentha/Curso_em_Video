#crie um conversor de dollar para real
num_dollar = float(input('Digite o valor em dollar US$: '))
num_real = (num_dollar * 5)
print('O valor em US$ é: {:.2f}\nconvertido para R$ é: {:.2f}'.format(num_dollar, num_real))
#lembre-se que eu definir o dolar  a 5.00, de forma arbitraria
#em uma aplicacao real, o valor do dolar e variavel, e o mesmo seria definido por uma API de consulta
