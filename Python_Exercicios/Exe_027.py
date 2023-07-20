#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
#último nome separadamente
nome_completo = input('Digite seu nome completo: ').strip().split()
print('Seu primeiro nome é: {}'.format(nome_completo[0]))
print('Seu ultimo nome é: {}'.format(nome_completo[len(nome_completo)-1]))

'''
nome_completo2 = input('Digite seu nome completo: ').strip() # remove os espaços do inicio e do fim
if len(nome_completo2.split()) == 0: # verifica se o nome tem apenas um elemento
    print('Voce nao digitou um nome')
elif len(nome_completo2.split()) == 1: # verifica se o nome tem apenas um elemento
    print('Voce digitou apenas um nome: {}'.format(nome_completo2.split()[0]))
else:
    print('Seu primeiro nome: {}\nSeu ultimo nome: {}'.format(nome_completo2.split()[0], nome_completo2.split()[-1]))
'''