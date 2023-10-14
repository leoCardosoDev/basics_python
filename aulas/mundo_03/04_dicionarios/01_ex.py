pessoas = {
  'nome': 'Leo',
  'sexo': 'M',
  'idade': 22
}

del pessoas['sexo']
pessoas['nome'] = 'Outro nome'
pessoas['peso'] = 98.5
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
  print(k)

for v in pessoas.values():
  print(v)

for k, v in pessoas.items():
  print(f'{k} = {v}')
