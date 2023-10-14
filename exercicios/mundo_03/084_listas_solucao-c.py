pessoas = []
total = 0
pesoMaior = []
pesoMenor = []

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Qual o seu peso? [Kg]: '))

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break

    pessoa = [nome, peso]
    pessoas.append(pessoa)

    if not pesoMaior or peso > max(pesoMaior, key=lambda x: x[1])[1]:
        pesoMaior = [pessoa]
    elif peso == max(pesoMaior, key=lambda x: x[1])[1]:
        pesoMaior.append(pessoa)

    if not pesoMenor or peso < min(pesoMenor, key=lambda x: x[1])[1]:
        pesoMenor = [pessoa]
    elif peso == min(pesoMenor, key=lambda x: x[1])[1]:
        pesoMenor.append(pessoa)

    total += 1

print(f'\nAo todo, você cadastrou {total} pessoas\n')

if pesoMaior:
    print(f'O maior peso foi de {max(pesoMaior, key=lambda x: x[1])[1]}kg')
    print(f'As pessoas com maior peso são: {[p[0] for p in pesoMaior]}')
else:
    print('Nenhuma pessoa cadastrada.')

if pesoMenor:
    print(f'O menor peso foi de {min(pesoMenor, key=lambda x: x[1])[1]}kg')
    print(f'As pessoas com menor peso são: {[p[0] for p in pesoMenor]}')
else:
    print('Nenhuma pessoa cadastrada.')
