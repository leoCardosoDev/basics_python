pesados = []
for p in range(0, 5):
    peso = float(input('Digite o peso de 5 pessoas (Kg): '))
    pesados.append(peso)
print(f'O maior peso tem {max(pesados)}Kg. O menor peso tem {min(pesados)}Kg')
