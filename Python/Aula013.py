#aula 13; modulo 2; curso em video
# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
# que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 11): # o ultimo numero não é contado
    print(c)
print('FIM')

for c in range(0, 11, 2): # o ultimo numero não é contado, e esta com um passo de 2
    print(c)

for c in range(10, 0, -1): # o ultimo numero não é contado, e esta com um passo de -1
    print(c)

numero_inicio = int(input('Digite o numero inicial: '))
numero_final = int(input('Digite o numero final: '))
numero_passo = int(input('Digite o numero do passo: '))
for c in range(numero_inicio, numero_final + 1, numero_passo): # o ultimo numero não é contado, e esta com um passo de -1
    print(c)
print('FIM')

somatorio = 0
for c in range(0, 3):# soma 3 numeros, o numero 0, 1 e 2
    numero = int(input('Digite um valor: '))
    somatorio += numero
print('O somatorio de todos os valores foi {}'.format(somatorio))

print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 46
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#  indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mContagem regressiva para o estouro de fogos de artifício\33[m')) # centraliza o texto
print('=#' * 35)
for aux in range(11, 0, -1):
    print("...{}".format(aux - 1)) # -1 para não mostrar o numero 11, e o 0 esta fora do range
    sleep(1)
print('what ....???')
sleep(2)
print('BUM! BUM! POOOW!')
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 47
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mNumeros pares entre 1 e 50\33[m')) # centraliza o texto
print('=#' * 35)
print('Os numeros pares entre 1 e 50 são:')
print('Processando ...')
sleep(2)
for aux in range(1, 51):
    if aux % 2 == 0:
        print(aux)
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 48
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
#  e que se encontram no intervalo de 1 até 500.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mSoma entre todos os números ímpares que são múltiplos de três\33[m')) # centraliza o texto
print('=#' * 35)
print('Os numeros impares entre 1 e 500 são:')
print('Processando ...')
sleep(2)
somatorio_mult3 = []
for aux in range(0, 501, 3): # o ultimo numero não é contado, e esta com um passo de 3
    if aux % 2 != 0: # se o numero for impar, pois o resto da divisão por 2 é diferente de 0
        somatorio_mult3.append(aux) # adiciona o valor na lista
print('Esses numeros são multiplos de 3 e impares: {}'.format(somatorio_mult3))
print('O somatorio de todos os valores foi {}'.format(sum(somatorio_mult3)))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 49
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
#  só que agora utilizando um laço for.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mTabuada\33[m')) # centraliza o texto
print('=#' * 35)
valor_tabuada = int(input('Digite o valor da tabuada: '))
print('Processando ...')
sleep(2)
for aux in range(0, 11):
    print('{} X {} = {}'.format(valor_tabuada, aux, valor_tabuada * aux))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 50
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mSoma dos numeros pares\33[m'))
print('=#' * 35)
somatorio_pares = []
print('Digite 6 numeros inteiros: ')
for aux in range(0, 6):
    valor_par = int(input('Digite o valor numero {}: '.format(aux + 1)))
    if valor_par % 2 == 0:
        somatorio_pares.append(valor_par) # adiciona o valor na lista
print('Processando ...')
sleep(2)
print('Os numeros pares digitados foram: {}'.format(somatorio_pares))
print('O somatorio dos numeros pares digitados foi: {}'.format(sum(somatorio_pares)))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
#  mostre os 10 primeiros termos dessa progressão.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mProgressão aritmética\33[m'))
print('=#' * 35)
primeiro_termo_pa = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
print('Processando ...')
sleep(2)
for aux in range(primeiro_termo_pa, primeiro_termo_pa + (razao_pa * 10), razao_pa):
    print(aux)
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mNumero primo\33[m'))
print('=#' * 35)
numero_primo = int(input('Digite um numero inteiro: '))
variavel_prima = 0
print('Agrupando ...')
sleep(1)
for aux in range(1, numero_primo + 1):
    if numero_primo % aux == 0:
        print('\33[30;42m{}\33[m'.format(aux), end=' ')# end=' ' para não quebrar a linha
        variavel_prima += 1
    else:
        print('\33[30;41m{}\33[m'.format(aux), end=' ')
print('\nVerificando ...')
sleep(2)
if variavel_prima % 2 == 0 and variavel_prima == 2:
    print('O numero {} é primo.'.format(numero_primo))
else:
    print('O numero {} não é primo.'.format(numero_primo))
print('\033[1;30;41m}#{|\033[m' * 20)

#desafio 53
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#  desconsiderando os espaços.
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

#desafio 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#  mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mMaioridade\33[m'))
print('=#' * 35)
from datetime import date
ano_atual = date.today().year # pega o ano atual
lista_ano_nascimento = []
maioridade = 0
print('Digite o ano de nascimento de 6 pessoas: ')
for aux in range(0, 6):
    ano_nascimento = int(input('Digite o ano de nascimento da pessoa {}: '.format(aux + 1)))
    lista_ano_nascimento.append(ano_nascimento)
len_lista_ano_nascimento = len(lista_ano_nascimento)
for aux in range(0, len_lista_ano_nascimento):
    if ano_atual - lista_ano_nascimento[aux] >= 18:
        maioridade += 1
print('Processando ...')
sleep(2)
print('Das {} pessoas, {} são maiores de idade e {} são menores de idade.'.format(len_lista_ano_nascimento, maioridade, len_lista_ano_nascimento - maioridade))
print ('\033[1;30;41m}#{|\033[m' * 20)

#desafio 55
# Faça um programa que leia o peso de cinco pessoas. No final,
#  mostre qual foi o maior e o menor peso lidos.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mMaior e menor peso\33[m'))
print('=#' * 35)
lista_de_pesos = []
for aux in range(0, 5):
    peso = float(input('Digite o peso da pessoa {}: '.format(aux + 1)))
    lista_de_pesos.append(peso)
print('Processando ...')
sleep(2)
print('O maior peso foi: {}Kg'.format(max(lista_de_pesos)))
print('O menor peso foi: {}Kg'.format(min(lista_de_pesos)))
print ('\033[1;30;41m}#{|\033[m' * 20)

#desafio 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('=#' * 35)
print('{:=^81}'.format('\33[30;42mAnalisador completo\33[m'))
print('=#' * 35)
#usando dicionarios
pessoas = {}
lista_de_pessoas = []
soma_idade = 0
for aux in range(0, 4):
    pessoas['nome'] = str(input('Digite o nome da pessoa {}: '.format(aux + 1))) 
    pessoas['idade'] = int(input('Digite a idade da pessoa {}: '.format(aux + 1)))
    pessoas['sexo'] = str(input('Digite o sexo da pessoa {}: '.format(aux + 1)))
    lista_de_pessoas.append(pessoas.copy())
    soma_idade += pessoas['idade']
print('Processando ...')
sleep(2)
print('A media de idade do grupo é: {}'.format(soma_idade / 4))
print('O nome do homem mais velho é: {}'.format(max(lista_de_pessoas, key=lambda x:x['idade'])['nome'])) # usando lambda, para pegar o maior valor de idade
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(min(lista_de_pessoas['idade'])))

