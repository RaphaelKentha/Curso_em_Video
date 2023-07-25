# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: {:.1f} Abaixo do Peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f} Peso Ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.1f} Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f} Obesidade'.format(imc))
else:
    print('IMC: {:.1f} Obesidade Mórbida'.format(imc))

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mCalculadora de IMC\33[m')
print('=$'*40)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
print('Calculando...')
sleep(1)
imc = peso / (altura ** 2) #altura elevado ao quadrado
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está \33[0;30;41mABAIXO DO PESO\33[m.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, você está no \33[0;30;42mPESO IDEAL\33[m.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}, você está com \33[0;30;43mSOBREPESO\33[m.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}, você está com \33[0;30;44mOBESIDADE\33[m.'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com \33[0;30;45mOBESIDADE MÓRBIDA\33[m.'.format(imc))
print('=$'*40)
'''
