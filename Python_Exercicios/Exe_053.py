# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase_palindromo = input('Digite uma frase: ').strip().upper()
frase_sem_espaco = frase_palindromo.replace(' ', '') # remove os espaços
frase_invertida_sem_espaco = frase_sem_espaco[::-1] # inverte a frase sem espaço
if frase_sem_espaco == frase_invertida_sem_espaco:
    print('A frase {} é um palindromo'.format(frase_palindromo))
else:
    print('A frase {} não é um palindromo'.format(frase_palindromo))
# o exemplo deveria ser feito usando for

for aux in range(0, len(frase_palindromo)):
    if frase_palindromo[aux] == frase_palindromo[-(aux + 1)]:
        print('A frase {} é um palindromo'.format(frase_palindromo))
        break
    else:
        print('A frase {} não é um palindromo'.format(frase_palindromo))
        break

# meu codigo:
'''	
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mPalíndromo\33[m'))
print('=#' * 35)
frase_palindromo = str(input('Digite uma frase: ')).strip().upper() # strip() para remover os espaços, upper() para deixar tudo em maiusculo
frase_palindromo_sem_espaco = frase_palindromo.replace(' ', '') # replace() para remover os espaços
frase_palindromo_invertida = frase_palindromo_sem_espaco[::-1] # [::-1] para inverter a frase
print('Processando ...')
sleep(2)
if frase_palindromo_sem_espaco == frase_palindromo_invertida:
    print('A frase {} é um palíndromo.'.format(frase_palindromo))
else:
    print('A frase {} não é um palíndromo.'.format(frase_palindromo))
print('\033[1;30;41m}#{|\033[m' * 20)
fiz o codigo sem usar o for
'''