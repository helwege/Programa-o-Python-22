'''
  Aula 17 - com plus
    Trabalhando com variaveis e seus tipos'''

nome = input('Qual é o seu nome?')
ano_nascimento = input('Que ano você nasceu?')
idade = 2022 - int(ano_nascimento)
idade = str(idade)
cidade = input('Onde você mora?')

print('O '+ nome + ' tem ' + idade + ' anos e mora em ' + cidade + '.')
