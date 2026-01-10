#desafio 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#simulando um modulo
#esse modulo é um arquivo .py que contem as funções abaixo
#o arquivo se chama moeda.py, e está na mesma pasta que esse arquivo
#para importar o modulo, basta usar o comando import moeda


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
#fim domodulo mopeda.py

#esse é o arquivo principal, que importa o modulo moeda.py
#para importar o modulo, basta usar o comando import moeda

# import moeda

print(f'Aumentar 10% de 100 é {aumentar(100, 10)}')
print(f'Diminuir 10% de 100 é {diminuir(100, 10)}')
print(f'O dobro de 100 é {dobro(100)}')
print(f'A metade de 100 é {metade(100)}')