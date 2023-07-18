#faca um programa que leia um numero, e mostre o numero, seu antecessor e sucessor
num = int(input('Digite um numero: '))
num_ant = num - 1
num_suc = num + 1
print('O numero digitado foi: {}\nseu antecessor é: {}\nseu sucessor é: {}'.format(num, num_ant, num_suc))

#em sua contra parte, feita nos desafios da aula 7:
'''
num_int = float(input('Digite um numero inteiro: '))
print('Passo define a razão de saida do programa!')
passo = float(input('Defina o passo: '))
num_int_suc = (num_int + passo)
num_int_ant = (num_int - passo)
'''
#fiz da forma acima, para que o usuario possa definir o passo, e assim, o programa possa ser mais dinamico