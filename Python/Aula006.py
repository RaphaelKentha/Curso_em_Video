#Aula 06, modulo 1
#Tipos primitivos
#int, float, bool, str
#[7, 7.9, True, 'txt']
#
#voltando para o ultimo exemplo da aula anterior(aul4)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
result = n1 + n2
print('A soma de {} e {} e: {}'.format(n1, n2, result))
#.format e mais pytonico!

#desafio:faca um programa que 'entenda' o que voce digitou
#para 'entender', vou utilizas o metodo: .is...

alguma_Coisa = input('Digite algo: ')
print(alguma_Coisa, 'é ', type(alguma_Coisa))
if alguma_Coisa.isalnum() == True:
    print(alguma_Coisa,'é um numero')
elif alguma_Coisa.isalpha() == True:
    print(alguma_Coisa,'é uma string')
else:
    print(alguma_Coisa,'é um Alfanumerico')

#tenho que melhorar esse codigo

print(type(alguma_Coisa.isalnum()))
print(alguma_Coisa.isalnum())