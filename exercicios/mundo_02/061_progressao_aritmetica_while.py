primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
c = primeiro
while c <= decimo:
  print(f'{c}', end=' -> ')
  c += razao
