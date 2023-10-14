estado = dict()
brasil = list()
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado. Ex: [SP]: '))
  brasil.append(estado.copy())

for lista in brasil:
  for dicionarioKey, dicionarioValue in lista.items():
    print(f'{dicionarioKey} - {dicionarioValue} ', end='')
  print()

for lista in brasil:
  for dicionarioValue in lista.values():
    print(f'{dicionarioValue} ', end='')
  print()
