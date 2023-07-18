#faca um codigo que converta de graus celsius para fahrenheit e kelvin
print('#' * 30)
print('Conversor de temperatura')
print('#' * 30)
print('Escolha uma das opcoes abaixo:\n1 - Celsius para Fahrenheit\n2 - Celsius para Kelvin\n3 - Fahrenheit para Celsius\n4 - Fahrenheit para Kelvin\n5 - Kelvin para Celsius\n6 - Kelvin para Fahrenheit')
opcao = int(input('Digite a opcao desejada: '))
if opcao == 1:
    opcao1 = float(input('Digite a temperatura em Celsius: '))
    opcao1_f = ((opcao1 * 9) / 5) + 32
    print('A temperatura em Fahrenheit é: {:.2f}°F'.format(opcao1_f))
elif opcao == 2:
    opcao2 = float(input('Digite a temperatura em Celsius: '))
    opcao2_k = (opcao2 + 273.15)
    print('A temperatura em Kelvin é: {:.2f}K'.format(opcao2_k))
elif opcao == 3:
    opcao3 = float(input('Digite a temperatura em Fahrenheit: '))   
    opcao3_c = ((opcao3 - 32) * 5) / 9
    print('A temperatura em Celsius é: {:.2f}°C'.format(opcao3_c))
elif opcao == 4:
    opcao4 = float(input('Digite a temperatura em Fahrenheit: '))
    opcao4_k = (((opcao4 - 32) * 5) / 9) + 273.15
    print('A temperatura em Kelvin é: {:.2f}K'.format(opcao4_k))
elif opcao == 5:
    opcao5 = float(input('Digite a temperatura em Kelvin: '))
    opcao5_c = (opcao5 - 273.15)
    print('A temperatura em Celsius é: {:.2f}°C'.format(opcao5_c))
elif opcao == 6:
    opcao6 = float(input('Digite a temperatura em Kelvin: '))
    opcao6_f = (((opcao6 - 273.15) * 9) / 5) + 32
    print('A temperatura em Fahrenheit é: {:.2f}°F'.format(opcao6_f))
else:
    print('Opcao invalida, tente novamente')

#tem formas mais simples de fazer esse codigo, porem, eu quis fazer dessa forma, para treinar o uso de if, elif e else
#veja um exemplo abaixo:
'''
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
'''
#resolve o problema de forma mais simples, porem, nao tem o uso de if, elif e else