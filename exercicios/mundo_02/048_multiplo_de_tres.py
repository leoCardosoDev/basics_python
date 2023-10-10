m3 = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont+=1
        m3 += c
print(f'A soma de todos os {cont} multiplos de 3 é: {m3}')
