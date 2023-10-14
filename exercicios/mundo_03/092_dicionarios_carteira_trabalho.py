from datetime import date
trabalhador = {}

nome = str(input('Nome: '))
trabalhador['nome'] = nome
data_nasc = int(input('Ano de nascimento: '))
idade = date.today().year - data_nasc
trabalhador['idade'] = date.today().year - data_nasc
carteira_trabalho = int(input('Carteira de trabalho (0 não tem): '))
if carteira_trabalho != 0:
  trabalhador['doc'] = carteira_trabalho
  ano_contratacao = int(input('Ano de contratação: '))
  trabalhador['ano_contratacao'] = ano_contratacao
  trabalhador['aposentar'] = (ano_contratacao + 35) - data_nasc


for key, value in trabalhador.items():
  if key not in 'doc':
    print(f'O {key} tem o valor {value}')
  else:
    print(f'O {key} tem o valor {value}')
