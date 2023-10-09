from datetime import date
maiores = []
menores = []
for n in range(0, 7):
    ano = int(input('Digite um ano de nascimento de alguém: '))
    if date.today().year - ano >= 21:
        maiores.append(n)
    else:
        menores.append(n)
print(
    f'Das 7 pessoas {len(maiores)} são maiores de idade e {len(menores)} são menores de idade')
