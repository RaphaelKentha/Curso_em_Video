#desafio 110
#Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from Exe_109 import moeda, aumentar, diminuir, dobro, metade
#funcoes definidas no Exe_109.py

def resumo(preco=0, aumento=0, reducao=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print(f'Aumento de {aumento}%: {aumentar(preco, aumento, True)}')
    print(f'Redução de {reducao}%: {diminuir(preco, reducao, True)}')
    print('-'*30)

resumo(100, 10, 10)