# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while

aux_while = 0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

while aux_while != 10:
    print(primeiro_termo)
    primeiro_termo += razao
    aux_while += 1

# meu codigo:
'''
from time import sleep
print('#=' * 35)
print('{:=^81}'.format('\33[30;42m10 Termos da PA\33[m'))
print('#=' * 35)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
print('Aguarde...')
sleep(1)
aux_while = 0
while aux_while != 10:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao_pa
    aux_while += 1
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)
'''