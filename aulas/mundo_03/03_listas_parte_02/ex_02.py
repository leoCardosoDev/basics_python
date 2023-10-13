galera = [['João', 19], ['Ana', 33], ['Joquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

print('\n')
print('-> - '* 35)

for pessoa in galera:
  print(pessoa)

for pessoa in galera:
  print(f'Nome: {pessoa[0]}, Idade: {pessoa[1]}')
