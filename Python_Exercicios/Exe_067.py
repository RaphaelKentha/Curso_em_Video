# Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando o número 
# solicitado for negativo

while True:
    numero_tabuada = int(input('Digite um número para ver sua tabuada: '))
    if numero_tabuada < 0:
        break
    else:
        for aux in range(1, 11):
            print(f'{numero_tabuada} x {aux} = {numero_tabuada * aux}')