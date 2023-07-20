#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
cidade = input('Digite o nome da cidade: ')
print('A cidade começa com a palavra Santo? {}'.format(cidade.split()[0].upper() == 'SANTO'))

'''
receba_nome_cidade = input('Digite o nome de uma cidade: ').strip() # remove os espaços do inicio e do fim
print('SANTO' in receba_nome_cidade.upper().split()[0]) # verifica se o primeiro elemento da lista em maiusculo contem 'SANTO'
if ('SANTO' in receba_nome_cidade.upper().split()[0]) == True:
    print('A cidade: {} comeca com o nome SANTO'.format(receba_nome_cidade.upper()))
else:
    print('A cidade: {} nao comeca com o nome SANTO'.format(receba_nome_cidade.upper()))
'''