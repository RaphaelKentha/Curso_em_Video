#desafio 86
#Crie um programa que crie uma matriz de dimensão 3x3 e 
# preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
zaux = 0
zaux2 = 0
zaux3 = 0
for aux in range(1, 10):
    if aux <= 3:
        num = int(input(f'Digite um valor para [0, {zaux}]: '))
        zaux += 1
        linha1.append(num)
    elif aux <= 6:
        num = int(input(f'Digite um valor para [1, {zaux2}]: '))
        zaux2 += 1
        linha2.append(num)
    else:
        num = int(input(f'Digite um valor para [2, {zaux3}]: '))
        zaux3 += 1
        linha3.append(num)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')