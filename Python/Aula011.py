# Aula 11; modulo 1; curso em video
# |Cores no terminal|
# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para
# configurar cores para os seus programas em Python. Veja como utilizar o código
# \033[m com todas as suas principais possibilidades.
# pesquisar sobre o modulo colorize

# \033[0;33;44m
# Style; Text; Back
# o Style pode ser:
# 0 - none
# 1 - bold
# 4 - underline
# 7 - negative
# o Text pode ser:
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - roxo
# 36 - ciano
# 37 - cinza
# o Back pode ser:
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul

print('\033[0;30;41mTeste\033[m') # e a cor, vermelho
print('\033[4;33;44mTeste\033[m') # e a cor, azul
print('\033[1;35;43mTeste\033[m') # e a cor, amarelo
print('\033[30;42mTeste\033[m') # e a cor, verde
print('\033[mTeste\033[m') # e a cor, branco
print('\033[7;30mTeste\033[m') # e a cor, preto
