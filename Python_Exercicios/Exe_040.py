# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

# meu codigo:
'''
from time import sleep
print('=$'*40)
print('\t\t\t\33[30;42mMédia Escolar\33[m')
print('=$'*40)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('Aguarde...')
sleep(1)
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi {:.1f}, você está \33[0;30;41mREPROVADO\33[m.'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi {:.1f}, você está de \33[0;30;43mRECUPERAÇÃO\33[m.'.format(media))
else:
    print('Sua média foi {:.1f}, você está \33[0;30;42mAPROVADO\33[m.'.format(media))
print('=$'*40)
'''