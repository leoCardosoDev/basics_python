alunos = {}
alunos['nome'] = str(input('Nome: '))
media = float(input('Média: '))
alunos['media'] = media

if media > 5.0:
  alunos['situacao'] = 'Aprovado'
else:
  alunos['situacao'] = 'Reprovado'

print(f'O nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]:.1f}')
print(f'Situação é igual a {alunos["situacao"]}')
