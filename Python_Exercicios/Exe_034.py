# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
#o aumento é de 15%.
from time import sleep
salario = float(input('Digite o salário do funcionário: '))
print('Calculando...')
sleep(3)
if salario > 1250:
    print('O salário do funcionário é de R${:.2f} e com o aumento de 10% passará a ser R${:.2f}'.format(salario, salario * 1.1))
else:
    print('O salário do funcionário é de R${:.2f} e com o aumento de 15% passará a ser R${:.2f}'.format(salario, salario * 1.15))
print('Fim do programa')

# Meu codigo abaixo:
'''
# Leia o salario de um funcionario e calcule o aumento
# para salarios superiores a 1250,00 o aumento e de 10%
# para salarios inferiores ou iguais a 1250,00 o aumento e de 15%
leia_salario = float(input('Digite o salario do funcionario: '))
if leia_salario > 0 and leia_salario <= 1250:
    print('O salario do funcionario apos o aumento e: {:.2f} Reai$'.format(leia_salario * 1.15))
elif leia_salario > 1250:
    print('O salario do funcionario apos o aumento e: {:.2f} Reai$'.format(leia_salario * 1.10))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)
'''