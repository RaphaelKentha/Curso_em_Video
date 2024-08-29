#desafio 97
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
#  mensagem com tamanho adaptável.

def escreva_adaptavel(texto):
    aux = len(texto) + 4
    print('Texto Formatado:')
    print('~' * aux)
    print(f'  {texto}')
    print('~' * aux)
#faz a função escreva_adaptavel ler o tamanho do texto e
#  adicionar 4 espaços a mais para o tamanho da linha

print('Escreva um texto qualquer')
texto = str(input('Digite um texto: '))
escreva_adaptavel(texto)