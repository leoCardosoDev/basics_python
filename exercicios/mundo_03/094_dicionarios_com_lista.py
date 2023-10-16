pessoas = []
pessoa = {}

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    pessoas.append(pessoa.copy())
    if continuar not in 'S':
        break
soma = 0
mulheres = []
for i in range(0, len(pessoas)):
    soma += pessoas[i]['idade']
    if 'F' in pessoas[i]['sexo']:
        mulheres.append(pessoas[i]["nome"])
media = soma / len(pessoas)

print(f'O grupo tem {len(pessoas)} pessoas')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(f'{mulher}, ', end='')
print()
print('A lista de pessoas acima da média: ')
for person in pessoas:
    if person['idade'] > media:
        print(f'Nome: {person["nome"]}, Sexo: {person["sexo"]}, Idade: {person["idade"]};')
        print()
