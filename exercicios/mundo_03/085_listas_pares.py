par_e_impar = []
pares = []
impares = []

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
        pares.sort()
    else:
        impares.append(num)
        impares.sort()

if pares:
    par_e_impar.insert(0, pares)
if impares:
    par_e_impar.insert(1, impares)

print(f'Os valores pares digitados foram: {par_e_impar[0]}')
print(f'Os valores impares digitados foram: {par_e_impar[1]}')
