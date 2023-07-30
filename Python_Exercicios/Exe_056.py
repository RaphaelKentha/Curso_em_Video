# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

soma_idade = 0
idade_homen_mais_velho = 0
numero_mulheres_menos_20 = 0
for aux in range(0, 4):
    nome = str(input('Digite o nome da {} pessoa: '.format(aux + 1))).strip()
    idade = int(input('Digite a idade da {} pessoa: '.format(aux + 1)))
    sexo = str(input('Digite o sexo da {} pessoa [M/F]: '.format(aux + 1))).strip().upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > idade_homen_mais_velho:
            idade_homen_mais_velho = idade
            nome_homen_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            numero_mulheres_menos_20 += 1
print('A média de idade do grupo é de {} anos.'.format(soma_idade / 4))
print('O nome do homem mais velho é {}.'.format(nome_homen_mais_velho))
print('O número de mulheres com menos de 20 anos é {}.'.format(numero_mulheres_menos_20))

# Explicacao do codigo acima, segundo "gpto":
'''	
Esse código é um programa Python que solicita informações sobre um grupo de pessoas e realiza algumas 
análises com base nos dados fornecidos. Vamos explicá-lo passo a passo:

1. Inicialização de variáveis:
   - `idade_homen_mais_velho`: Variável que armazenará a idade do homem mais velho. Inicialmente, 
   é definida como zero.
   - `numero_mulheres_menos_20`: Variável que contará o número de mulheres com menos de 20 anos. 
   Inicialmente, é definida como zero.

2. Loop `for`:
   - `for aux in range(0, 4):`: Esse loop vai iterar quatro vezes, coletando informações sobre quatro pessoas.

3. Entrada de dados:
   - Para cada iteração do loop, o programa solicita ao usuário que insira os seguintes dados:
     - `nome`: Nome da pessoa.
     - `idade`: Idade da pessoa.
     - `sexo`: Sexo da pessoa (M para masculino e F para feminino).
   - As informações são armazenadas nas variáveis correspondentes.

4. Cálculo da média de idade:
   - `soma_idade += idade`: Aqui, a idade fornecida é somada à variável `soma_idade`, que acumula a soma 
   de todas as idades.

5. Análise de homens mais velhos:
   - O programa verifica se a pessoa é do sexo masculino (`if sexo == 'M':`).
   - Se sim, compara a idade dessa pessoa com a idade registrada em `idade_homen_mais_velho`.
   - Se a idade atual for maior que a idade do homem mais velho registrada até o momento, a idade e o 
   nome do homem mais velho são atualizados.

6. Contagem de mulheres com menos de 20 anos:
   - O programa verifica se a pessoa é do sexo feminino (`elif sexo == 'F':`).
   - Se sim, verifica se a idade da pessoa é menor que 20 anos.
   - Caso seja verdadeiro, incrementa em 1 a variável `numero_mulheres_menos_20`, que conta 
   o número de mulheres com menos de 20 anos.

7. Exibição dos resultados:
   - Fora do loop, após a coleta de todas as informações, o programa exibe os resultados:
     - A média de idade do grupo é calculada e exibida como `soma_idade / 4`.
     - O nome do homem mais velho é exibido como `nome_homen_mais_velho`.
     - O número de mulheres com menos de 20 anos é exibido como `numero_mulheres_menos_20`.

É importante notar que o código utiliza uma lista de tamanho fixo (4 pessoas) para realizar as análises. 
Caso deseje analisar mais pessoas, o código precisaria ser adaptado para armazenar as informações em 
uma estrutura de dados dinâmica, como uma lista ou dicionário, para que os resultados sejam corretos para 
qualquer quantidade de pessoas
'''
# Inicialização das listas vazias para armazenar os dados
nomes_masc = []
nomes_fem = []
idades_masc = []
idades_fem = []
sexos = []

# Entrada de dados
numero_pessoas = int(input("Digite o número de pessoas no grupo: "))
for i in range(numero_pessoas):
    nome = input("Digite o nome da {}ª pessoa: ".format(i + 1)).strip()
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i + 1)))
    sexo = input("Digite o sexo da {}ª pessoa [M/F]: ".format(i + 1)).strip().upper()
    if sexo == 'M':
        nomes_masc.append(nome)
        idades_masc.append(idade)
    elif sexo == 'F':
        nomes_fem.append(nome)
        idades_fem.append(idade)
    sexos.append(sexo)

# Análise dos dados
media_idade = sum(idades_fem) + sum(idades_masc) / numero_pessoas
homem_mais_velho_idade = max(idades_masc)
homem_mais_velho_nome = nomes_masc[idades_masc.index(homem_mais_velho_idade)] # idade do homem mais velho, se houver mais de um, retorna o primeiro
mulheres_menos_20 = sum(1 for idade in idades_fem if idade < 20 and sexos[idades_fem.index(idade)] == 'F')

# Exibição dos resultados
print("\nResultados:")
print("A média de idade do grupo é de {:.2f} anos.".format(media_idade))
print("O nome do homem mais velho é {} com {} anos.".format(homem_mais_velho_nome, homem_mais_velho_idade))
print("O número de mulheres com menos de 20 anos é {}.".format(mulheres_menos_20))
