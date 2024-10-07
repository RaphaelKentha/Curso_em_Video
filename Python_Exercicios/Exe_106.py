#desafio 106
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará

def helpy():
    """ 
    Função que ajuda o usuário a entender o que cada função do python faz.
    :return: None
    """
    print('\33[0;30;42mSistema de ajuda PyHelp\33[m')
    while True:
        comando = input('Função ou Biblioteca > ')
        if comando.upper() == 'FIM':
            print('\33[0;30;41mAté logo!\33[m')
            break
        else:
            print('\33[0;30;44m')
            help(comando)
            print('\33[m')

helpy()
