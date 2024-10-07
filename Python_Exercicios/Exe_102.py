#desafio 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    f=1
    for aux in range(numero, 0, -1):
        if show:
            print(aux, end='')
            if aux > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= aux
    return f

print(fatorial(5, show=True))
print(fatorial(5, show=False))
