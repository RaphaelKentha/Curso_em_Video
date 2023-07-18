#leia o preco de um produto em reais, e aplique um desconto
preco = float(input('Digite o valor do produto R$: '))
desconto = float(input('Digite o valor do desconto: '))
preco_final = preco - (preco *(desconto / 100))
print('O valor do produto é: R${:.2f}\nO desconto é: {:.2f}%\nO valor final é: R${:.2f}'.format(preco, desconto, preco_final))