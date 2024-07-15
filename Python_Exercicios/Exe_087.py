#desafio 87
#Aprimore o desafio anterior (86), mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
pares = []
soma_terceira_coluna = 0
zaux = 0
zaux2 = 0
zaux3 = 0
for aux in range(1, 10):
    if aux <= 3:
        num = int(input(f'Digite um valor para [0, {zaux}]: '))
        if num % 2 == 0:
            pares.append(num)
        zaux += 1
        linha1.append(num)
    elif aux <= 6:
        num = int(input(f'Digite um valor para [1, {zaux2}]: '))
        if num % 2 == 0:
            pares.append(num)
        zaux2 += 1
        linha2.append(num)
    else:
        num = int(input(f'Digite um valor para [2, {zaux3}]: '))
        if num % 2 == 0:
            pares.append(num)
        zaux3 += 1
        linha3.append(num)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma dos valores pares é: {sum(pares)}')
soma_terceira_coluna = linha1[2] + linha2[2] + linha3[2]
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {max(linha2)}')