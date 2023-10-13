continuar = 'S'
valores = []
par = []
impar = []

while True:
  if continuar not in 'S':
    break
  valores.append(int(input('Digite um número: ')))
  continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'A lista completa é: {valores}')
for parOuImpar in valores:
  if parOuImpar % 2 == 0:
    par.append(parOuImpar)
  else:
    impar.append(parOuImpar)
print(f'A lista completa de pares é: {par}')
print(f'A lista de impares é: {impar}')
