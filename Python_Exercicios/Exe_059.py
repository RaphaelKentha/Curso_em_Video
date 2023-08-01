# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print('[1] soma\n[2] multiplicação\n[3] maior\n[4] novos números\n[5] sair do programa')
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print('A soma entre {} e {} é {}'.format(numero1, numero2, numero1 + numero2))
elif opcao == 2:
    print('A multiplicação entre {} e {} é {}'.format(numero1, numero2, numero1 * numero2))
elif opcao == 3:
    if numero1 > numero2:
        print('O maior número entre {} e {} é {}'.format(numero1, numero2, numero1))
    else:
        print('O maior número entre {} e {} é {}'.format(numero1, numero2, numero2))
elif opcao == 4:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    print('[1] soma\n[2] multiplicação\n[3] maior\n[4] novos números\n[5] sair do programa')
    opcao = int(input('Digite a opção desejada: '))
elif opcao == 5:
    print('Fim do programa')
else:
    print('Opção inválida, tente novamente!')

# fiz o codigo co if, pois o while nessas condições não é necessário
# meu codigo com while:
'''
from time import sleep
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
print('Aguarde...')
sleep(0.5)
print('O que você deseja fazer com os numeros {} e {}?'.format(numero_1, numero_2))
print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
opcao = int(input('Digite a opção desejada: '))
while validacao_calculadora == 0:
    if opcao == 1:
        print('Somando...')
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(numero_1, numero_2, numero_1 + numero_2))
        validacao_calculadora = 1
    elif opcao == 2:
        print('Multiplicando...')
        sleep(0.5)
        print('A multiplicação entre {} e {} é {}'.format(numero_1, numero_2, numero_1 * numero_2))
        validacao_calculadora = 1
    elif opcao == 3:
        print('Verificando...')
        sleep(0.5)
        if numero_1 > numero_2:
            print('O numero {} é maior que {}'.format(numero_1, numero_2))
            validacao_calculadora = 1
        elif numero_2 > numero_1:
            print('O numero {} é maior que {}'.format(numero_2, numero_1))
            validacao_calculadora = 1
        else:
            print('Os numeros são iguais')
            validacao_calculadora = 1
    elif opcao == 4:
        print('Reiniciando...')
        sleep(0.5)
        numero_1 = int(input('Digite o primeiro numero: '))
        numero_2 = int(input('Digite o segundo numero: '))
        print('Aguarde...')
        sleep(0.5)
        print('O que você deseja fazer com os numeros {} e {}?'.format(numero_1, numero_2))
        print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao = int(input('Digite a opção desejada: '))
    elif opcao == 5:
        print('Saindo...')
        sleep(0.5)
        validacao_calculadora = 1
print('\033[1;30;41m}#{|\033[m' * 20)

# meu codigo com while e lista:
# codigo abaixo é o mesmo do de cima usando lista
lita_numero = []
elemnto1 = int(input('Digite o primeiro numero: '))
lita_numero.append(elemnto1)
elemnto2 = int(input('Digite o segundo numero: '))
lita_numero.append(elemnto2)
validacao_lista = False
while validacao_lista == False:
    print( 'Escolha: [1] - soma, [2] - multiplicação, [3] - maior, [4] - novos numeros, [5] - sair do programa')
    opcao_lista = int(input('Digite a opção desejada: '))
    if opcao_lista == 1:
        print('Somando...')
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(elemnto1, elemnto2, sum(lita_numero)))
        validacao_lista = True
    elif opcao_lista == 2:
        print('Multiplicando...')
        sleep(0.5)
        print('A multiplicação entre {} e {} é {}'.format(elemnto1, elemnto2, elemnto1 * elemnto2))
        validacao_lista = True
    elif opcao_lista == 3:
        print('Verificando...')
        sleep(0.5)
        if elemnto1 == elemnto2:
            print('Os numeros são iguais')
            validacao_lista = True
        else:
            print('O maior numero entre {} e {} é {}'.format(elemnto1, elemnto2, max(lita_numero)))
    elif opcao_lista == 4:
        print('Reiniciando...')
        sleep(0.5)
        elemnto1 = int(input('Digite o primeiro numero: '))
        lita_numero.append(elemnto1)
        elemnto2 = int(input('Digite o segundo numero: '))
        lita_numero.append(elemnto2)
        print('Aguarde...')
        sleep(0.5)
        print('O que você deseja fazer com os numeros {} e {}?'.format(elemnto1, elemnto2))
        print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
        opcao_lista = int(input('Digite a opção desejada: '))
    elif opcao_lista == 5:
        print('Saindo...')
        sleep(0.5)
        validacao_lista = True
print('\033[1;30;41m}#{|\033[m' * 20)
'''