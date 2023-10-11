somaIdadeMais18 = 0
totalHomens = 0
mulheresMenor20 = 0
continua = 'S'

while True:
    if continua not in 'Ss':
        break
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if idade >= 18:
        somaIdadeMais18 += 1

    if sexo == 'M':
        totalHomens += 1
    
    if sexo == 'F' and idade <= 19:
        mulheresMenor20 += 1
        
print(f'Total de pessoas com mais de 18 anos: {somaIdadeMais18}')
print(f'Ao todo temos {totalHomens} homens cadastrados')
print(f'E temos {mulheresMenor20} mulheres com menos de 20 anos')
