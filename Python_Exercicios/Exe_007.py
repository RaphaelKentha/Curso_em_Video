#faca um codigo que leia as notas de um aluno, e mostre sua media e conceito
print('###########################################')
print('########## NOTAS E CONCEITOS ##############')
print('###########################################')
num_notas = int(input('Quantas notas deseja inserir? '))
nota_soma = 0
for i in range(0, num_notas):
    nota = float(input('Digite a nota{}: '.format(i+1)))
    nota_soma += nota
nota_media = (nota_soma / num_notas)
if nota_media >= 9:
    print('A media do aluno foi: {:.2f}\nO conceito do aluno foi: A'.format(nota_media))
elif nota_media >= 7.5 and nota_media < 9:
    print('A media do aluno foi: {:.2f}\nO conceito do aluno foi: B'.format(nota_media))
elif nota_media >= 6 and nota_media < 7.5:
    print('A media do aluno foi: {:.2f}\nO conceito do aluno foi: C'.format(nota_media))
elif nota_media >= 4 and nota_media < 6:
    print('A media do aluno foi: {:.2f}\nO conceito do aluno foi: D'.format(nota_media))
elif nota_media < 4:
    print('A media do aluno foi: {:.2f}\nO conceito do aluno foi: E'.format(nota_media))
print('###########################################')
#o codigo acima demonstra o uso de if, elif e else, para definir o conceito do aluno, de acordo com sua media
#ao passo que demora mais tempo para ser feito
#o codigo abaixo, faz a mesma coisa, porem, de forma mais rapida e simples
'''
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
print('Media da notas: {}'.format(media))
'''