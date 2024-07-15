#desafio 85
#Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os 
# valores pares e ímpares. No final, mostre os valores pares e ímpares 
# em ordem crescente.

lista_par = []
lista_impar = []
lista_total = [lista_par, lista_impar]

for aux in range(1, 8):
    num = int(input(f'Digite o {aux}º valor: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
lista_par.sort() #ordena a lista
lista_impar.sort() #ordena a lista
print(f'Os valores pares digitados foram: {lista_par}')
print(f'Os valores ímpares digitados foram: {lista_impar}')