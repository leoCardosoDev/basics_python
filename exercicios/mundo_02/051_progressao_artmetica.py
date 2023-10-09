print('='*15 + ' Inicio ' + '='*15)
print('an = a1 + (n-1) * d')
for c in range(1, 10+1):
    print(f'a{c} = a1 + d')
    if c >= 2:
        print(f'a{c} = a1 + {c}d')
print('='*15 + ' Encontrando os 10 termos ' + '='*15)
i = 2
a1 = 2
d = 3
print(f'a1 = {a1}')
for n in range(1, 10+1):
    if n == 2:
        print(f'a{n} = {a1} + {d} = {a1 + d}')
    if n >= 3:
        print(f'a{n} = {a1} + {i} x {d} = {a1 + i * d }')
        i += 1
print('='*15 + 'FIM ' + '='*15)
