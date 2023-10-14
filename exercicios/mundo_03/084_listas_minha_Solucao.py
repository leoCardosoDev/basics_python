pessoas = []
total = 0

while True:
  nome = str(input('Nome: ')).strip()
  peso = int(input('Peso: '))
  pessoa = [nome, peso]
  pessoas.append(pessoa)
  total += 1
  continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
  if continuar != 'S':
    break

print(f'Você cadastrou {total} de pessoas\n')
if pessoas:
  pessoa_maior_peso = max(pessoas, key=lambda x: x[1])
  pessoa_menor_peso = min(pessoas, key=lambda x: x[1])
  print(f'A pessoa com maior peso é {pessoa_maior_peso[0]} com {pessoa_maior_peso[1]}kg')
  print(f'A pessoa com menor peso é {pessoa_menor_peso[0]} com {pessoa_menor_peso[1]}kg')
else:
  print('Nenhuma pessoa cadastrada!')
