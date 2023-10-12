lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print('=' * 40)
print(lanche)

print('=' * 40)
print(lanche[1])

print('=' * 40)
print(lanche[-2])

print('=' * 40)
print(lanche[1:3])

print('=' * 40)
print(lanche[2:])

print('=' * 40)
print(lanche[:2])

print('=' * 40)
print(lanche[-2:])

print('=' * 40)
print(lanche[:-2])

for comida in lanche:
    print(f'{comida}')
print('=' * 40)

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}')
print('=' * 40)

for pos, comida in enumerate(lanche):
    print(f'{pos} - {comida}')
print('=' * 40)
print(sorted(lanche))
print('=' * 40)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
d = b + a
print(c)
print('=' * 40)
print(d)
print('=' * 40)
print(c.count(5))
print('=' * 40)
print(c.index(8))

print('=' * 40)
pessoa = ('Leo', 41, 96.5)
print(pessoa)
del (d)
# print(d)
