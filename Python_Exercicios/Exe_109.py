#desafio 109
#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    #facilita a formatação do preço

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

#caso o usuario informe True no parametro formato, o valor retornado será formatado pela função moeda

print(moeda(100))#R$100,00
print(aumentar(100, 10, True))#R$110,00
print(diminuir(100, 10, True))#R$90,00
print(dobro(100, True))#R$200,00
print(metade(100, True))#R$50,00
print(metade(100))#50.0
print(dobro(100))#200.0
print(diminuir(100, 10))#90.0
print(aumentar(100, 10))#110.0