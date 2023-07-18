#faca um codigo que calcula a area de uma parede, e a quantidade de tinta necessaria para pinta-la
#sabendo que um litro de tinte, pinta um area de dois metros quadrados
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = (altura * largura)
tinta = (area / 2)
print('A area da parede é: {:.2f}m²\nA quantidade de tinta necessaria para pinta-la é: {:.2f}L'.format(area, tinta))