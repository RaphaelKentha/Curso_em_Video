#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco = (km * 0.15) + (dias * 60)
print('O valor a pagar é: R${:.2f}'.format(preco))
#codigo mais direto e simples

#codigo mais dinamico:
print('Digite a opcao desejada: ')
opcao = input('O carro foi alugado por dias ou por Km:\n1 - dias \n2 - km')
if opcao == str(1):
    dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
    preco = (dias * 60) + 55
    print('O valor a pagar é: R${:.2f}'.format(preco))
elif opcao == str(2):
    km = float(input('Digite a quantidade de Km percorridos: '))
    preco = (km * 0.15) + 110
    print('O valor a pagar é: R${:.2f}'.format(preco))
else:
    print('Opcao invalida')