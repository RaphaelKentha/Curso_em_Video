# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    print('O valor da passagem é de R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor da passagem é de R${:.2f}'.format(distancia * 0.45))
print('Fim do programa')

# Meu codigo abaixo:
'''
 Calcule o preco de uma viagem, de acordo com a distancia percorrida
ate 200km, o km e cinquenta centavos acima de 200km o km e quarenta e cinco cents de dolar.


viagem_km = float(input('Digite a distancia da viagem em km: '))
valor_dollar = float(input('Digite o valor do dolar: '))
if viagem_km > 0 and viagem_km <= 200:
    print('O valor da viagem e: {:.2f} Reai$'.format(viagem_km * 0.5))
elif viagem_km > 200:  
    print('O valor da viagem e: {:.2f} Reai$'.format(viagem_km * 0.45*valor_dollar))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)

'''