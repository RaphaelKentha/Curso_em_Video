# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado! O valor da multa é de R${:.2f}'.format((velocidade - 80) * 7))
else:
    print('Você está dentro do limite de velocidade. Dirija com segurança!')
    print('Tenha um bom dia! Dirija com segurança!')
print('Fim do programa')

# Meu codigo abaixo:
'''
Leia a velocidade de um carro na estrada
se o mesmo ultrapassar 80 Km/h ele sera multado em 69 reais
por cada km/h acima do limite permitido.

velocidado_do_veiculo = float(input('Digite a velocidade do veiculo: '))
print('A velocidade maxima permitida e: 80 Km/h')
if velocidado_do_veiculo <= 80 and velocidado_do_veiculo >0:
    print('Parabens, voce esta dentro da velocidade permitida')
elif velocidado_do_veiculo > 80:
    print('Sua velocidade e: {} Km/h'.format(velocidado_do_veiculo))
    print('Voce foi multado em: {:.1f} Reai$'.format((velocidado_do_veiculo - 80) * 69,73))
else:
    print('Voce digitou um valor invalido')
print('Fim do programa')
print('#' * 50)
'''