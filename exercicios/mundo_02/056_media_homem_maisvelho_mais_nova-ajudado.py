somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulherNova = 0
for p in range(1, 5):
    print(f'_______ {p}ª PESSOA _______')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mn':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulherNova += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}')
print(f'Ao todo são {totalMulherNova} mulheres com menos de 20 anos')
