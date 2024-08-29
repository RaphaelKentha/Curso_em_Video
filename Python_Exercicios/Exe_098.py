#desafio 98
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize
# a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

def contador(inicio, fim , passo):
    print(f'Contagem {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
        for aux in range(inicio, fim + passo, passo):
            print(aux, end=' ')
    elif fim - inicio < 0:
        passo *= -1
        for aux in range(inicio, fim + passo, passo):
            print(aux, end=' ')
    elif fim - inicio > 0:
        for aux in range(inicio, fim + passo, passo):
            print(aux, end=' ')
    
    

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(0, 100, 10)
print()
contador(0, 100, 0)