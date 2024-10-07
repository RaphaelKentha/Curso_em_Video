#criando uma função chamada fatorial
def fatorial(numero):
    """
    -> Calcula o fatorial de um número.
    :param numero: o número a ser calculado
    :return: o fatorial do número
    """
    fator = 1
    for aux in range(numero, 0, -1):
        fator *= aux
    return fator
def dobro(numero):
    """
    -> Calcula o dobro de um número.
    :param numero: o número a ser calculado
    :return: o dobro do número
    """
    return numero * 2
def triplo(numero):
    """
    -> Calcula o triplo de um número.
    :param numero: o número a ser calculado
    :return: o triplo do número
    """
    return numero * 3