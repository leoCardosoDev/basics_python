from datetime import date
ano = int(input('Qual ano voce nasceu? '))
idade = date.today().year - ano


if idade < 18 and 18 - idade != 1:
    print('Presta atenção faltam {} anos para você se alistar!'.format(
        18 - idade))
elif idade < 18 and 18 - idade == 1:
    print('ATENÇÃO! Ano que vem você precisa se apresentar!')
elif idade == 18:
    print('ACORDA! Esse ano você precisa se apresentar!')
elif idade > 18 and idade - 18 < 3:
    print('PASSOU DA HORA RAPAZ! Está {} anos atrasado para você se apresentar'.format(
        idade - 18))
else:
    print('Você é um caso perdido!')
