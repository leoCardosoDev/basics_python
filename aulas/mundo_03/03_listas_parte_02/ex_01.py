teste = list()
teste.append('Leo')
teste.append(41)
print(teste)
print('_'*40)

galera = list()
galera.append(teste[:])
print(galera)

print('_'*40)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
