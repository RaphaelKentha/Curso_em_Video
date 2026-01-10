#desafio 108
# Adapte o código do Exe_107.py para que ele aceite um valor monetário e formate esse valor como um valor monetário.

import Exe_107
#temos acesso as funções do modulo moeda.py, que são aumentar(), diminuir(), dobro() e metade() descritas no Exe_107.py
#copia do arquivo Exe_107.py
'''
def aumentar(valor = 0, cambio = 0):
    """
    Função que aumenta um valor em uma porcentagem.
    no caso de moeda, o valor é o dinheiro e o cambio é a porcentagem.
    :param valor: float
    :param cambio: float
    :return: float
    """
    return valor + (valor * (cambio /100))

def diminuir(valor = 0, cambio = 0):
    """
    Função que diminui um valor em uma porcentagem.
    no caso de moeda, o valor é o dinheiro e o cambio é a porcentagem.
    :param valor: float
    :param cambio: float
    :return: float
    """
    return valor - (valor * (cambio /100))

def dobro(valor = 0):
    """
    Função que dobra um valor.
    no caso de moeda, o valor é o dinheiro.
    :param valor: float
    :return: float
    """
    return valor * 2

def metade(valor = 0):
    """
    Função que divide um valor pela metade.
    no caso de moeda, o valor é o dinheiro.
    :param valor: float
    :return: float
    """
    return valor / 2
'''


aumento = Exe_107.aumentar(100, 10)
reducao = Exe_107.diminuir(100, 10)
var_dobro = Exe_107.dobro(100)
var_metade = Exe_107.metade(100)
print(f'Aumentar 10% de 100 é {aumento:.2f}')
print(f'Diminuir 10% de 100 é {reducao:.2f}')
print(f'O dobro de 100 é {var_dobro:.2f}')
print(f'A metade de 100 é {var_metade:.2f}')