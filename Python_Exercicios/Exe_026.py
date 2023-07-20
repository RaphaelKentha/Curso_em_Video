#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez
frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

'''
leia_frase = input('Digite uma frase: ').strip() # remove os espaços do inicio e do fim

if len(leia_frase) == 1:  # conta a quantidade de vezes que a letra 'A' aparece na frase
    print('A letra "A" aparece {} vez na frase'.format(leia_frase.count('A')))
else:
    print('A letra "A" aparece {} vezes na frase'.format(leia_frase.count('A')))
print('A letra "A" aparece pela primeira vez na posicao {}'.format(leia_frase.find('A')+1)) # mostra a posicao da primeira vez que a letra 'A' aparece
print('A letra "A" aparece pela ultima vez na posicao {}'.format(leia_frase.rfind('A')+1)) # mostra a posicao da ultima vez que a letra 'A' aparece
#nota: o +1 foi utilizado para que a posicao seja mostrada a partir de 1 e nao de 0
#nota: o rfind() retorna a posicao da ultima vez que a letra 'A' aparece, pois comeca a contagem da direita(rigth)
'''