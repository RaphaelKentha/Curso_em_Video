#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome
nome = input('Digite seu nome: ').strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
#quando 'Silva' devemos utiliza o .capitalize() para que o programa funcione corretamente e um laco para verificar se o nome tem Silva

'''
leia_nome_pessoa = input('Digite o nome de uma pessoa: ').strip() # remove os espaços do inicio e do fim
print('SILVA' in leia_nome_pessoa.upper().split()) # verifica se a lista em maiusculo contem 'SILVA'
if ('SILVA' in leia_nome_pessoa.upper().split()) == True:
    print('O nome: {} tem SILVA'.format(leia_nome_pessoa.upper()))
else:
    print('O nome: {} nao tem SILVA'.format(leia_nome_pessoa.upper()))

para 'Silva'
leia_nome_pessoa = input('Digite o nome de uma pessoa: ').strip() # remove os espaços do inicio e do fim
for i in range(0, len(leia_nome_pessoa.split())): # para cada elemento da lista
    if leia_nome_pessoa.split()[i].capitalize() == 'Silva': # verifica se o elemento da lista e igual a 'Silva'
        print('O nome: {} tem Silva'.format(leia_nome_pessoa))
    else:
        print('O nome: {} nao tem Silva'.format(leia_nome_pessoa))
'''
