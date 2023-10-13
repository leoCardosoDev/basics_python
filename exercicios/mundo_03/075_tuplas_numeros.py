valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')),)

cont = 0
for par in range(0, len(valores)):
    if valores[par] % 2 == 0:
        cont += 1

print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez(es)')

if 3 in valores:
   print(f'O valor 3 foi digitado na {valores.index(3) + 1}ª posição')
else:
  print(f'O valor 3 NÃO foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram {cont}')
