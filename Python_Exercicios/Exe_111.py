#desafio 111
#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

#simulando um pacote
#esse pacote é uma pasta que contem os arquivos moeda.py e dado.py
#os arquivos estão na mesma pasta que esse arquivo
import Exe_109
#para importar o pacote, basta usar o comando import Exe_109.moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {Exe_109.moeda.moeda(preco)} é {Exe_109.moeda.metade(preco, True)}')
print(f'O dobro de {Exe_109.moeda.moeda(preco)} é {Exe_109.moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {Exe_109.moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {Exe_109.moeda.diminuir(preco, 13, True)}')