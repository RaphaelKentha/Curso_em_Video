#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido
import random
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.

'''
nomes = []
for i in range(0, 4):
    nomes[i] = input('Digite o nome: ')
print(nomes)
sorteado = random.randint(0, 3)
print('O sorteado foi: {}'.format(nomes[sorteado]))

para este exemplo, mesmo estando errado funciona para o exercicio
'''