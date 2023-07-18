#faca um algoritmo que leia um salario e faca um reajuste, para o aumento ou reducao do salario
salario = float(input('Digite o valor do salario R$: '))
ajuste = float(input('Digite o valor do ajuste: '))
condicao = input('O salario tera um aumento ou reducao de {:.2f}%: (aumento/reducao) '.format(ajuste))
if condicao == 'aumento':
    salario_final = salario + (salario * (ajuste / 100))
    print('O salario é: R${:.2f}\nO ajuste é: {:.2f}%\nO salario final é: R${:.2f}'.format(salario, ajuste, salario_final))
elif condicao == 'reducao':
    salario_final = salario - (salario * (ajuste / 100))
else:
    print('Opcao invalida')

#o codigo acima esta usando o if e elif, para fazer uma condicao, e assim, o programa possa ser mais dinamico
#no entanto uma sulocao para o problema:
'''
aumento = float(input('Digite o valor do aumento: '))
salario = float(input('Digite o valor do salario: '))
salario_aumento = salario + (salario * aumento / 100)
print('O valor do salario e: {} \nO valor do aumento e: {}% \nO valor do salario com aumento e: {}'.format(salario, aumento, salario_aumento))
'''
#e bem simples, entretanto resolve a questao, porem, nao e dinamico