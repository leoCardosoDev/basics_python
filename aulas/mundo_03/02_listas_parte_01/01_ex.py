num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 0)
num.insert(3, 4)
num.sort()
num.sort(reverse=True)
num.pop(0)
if 9 in num:
  num.remove(9)
else:
  print('-> -> Não achei o número 9 <- <-')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
