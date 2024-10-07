#desafio 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas_alunos(*notas, sit = False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict() # dicionário para armazenar as informações
    turma['total'] = len(notas) # quantidade de notas
    turma['maior'] = max(notas) # maior
    turma['menor'] = min(notas) # menor
    turma['média'] = sum(notas) / len(notas) # média
    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif 5 <= turma['média'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma

# consulta aluno
resp = notas_alunos(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas_alunos)
