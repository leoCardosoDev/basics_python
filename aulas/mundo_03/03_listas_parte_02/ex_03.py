galera = list()
dado = list()
maior = menor = 0

for c in range(0, 3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:])
  dado.clear()

print(dado)
print(galera)

print('\n')

for p in galera:
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade!')
    maior += 1
  else:
    print(f'{p[0]} é menor de idade!')
    menor += 1
print(f'Temos {maior} maiores e {menor} menores')
print('\n')
