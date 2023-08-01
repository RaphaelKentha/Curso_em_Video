# Perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos

aux_while = 0
print('Deseja alterar o numero de termos exibidos: \n[1] Sim \n[2] Não \n[0] fechar Programa')
alterar_termo = int(input('Digite a opção desejada:'))

if alterar_termo == 1:
    novo_termo = int(input('Digite o novo numero de termos: '))
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    while aux_while != novo_termo:
        print(primeiro_termo)
        primeiro_termo += razao
        aux_while += 1
elif alterar_termo == 2:
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    while aux_while != 10:
        print(primeiro_termo)
        primeiro_termo += razao
        aux_while += 1
elif alterar_termo == 0:
    print('Programa encerrado!')
    aux_while = 10
else:
    print('Opção inválida!')

# meu codigo:
'''
from time import sleep
print('#=' * 35)
print('{:=^81}'.format('\33[30;42mX Termos da PA\33[m'))
print('#=' * 35)
print('A configuração padrão é de 10 termos')
alteracao_n_termos = int(input('Deseja alterar a quantidade de termos? [1] - Sim, [2] - Não: '))
if alteracao_n_termos == 1:
    n_termos = int(input('Digite a quantidade de termos: '))    
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao_pa = int(input('Digite a razão da PA: '))
    print('Aguarde...')
    sleep(1)
    aux_while = 0
    while aux_while != n_termos:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao_pa
        aux_while += 1
else:
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao_pa = int(input('Digite a razão da PA: '))
    print('Aguarde...')
    sleep(1)
    aux_while = 0
    while aux_while != 10:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao_pa
        aux_while += 1
print('FIM')
print('\033[1;30;41m}#{|\033[m' * 20)
'''