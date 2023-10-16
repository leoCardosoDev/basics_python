def contador(*num):
  tam = len(num)
  for valor in num:
    print(f'{valor} ', end='')
  print()
  print(f'Recebo os valores {num} e são ao todo {tam} números')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
