a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

c = [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')
