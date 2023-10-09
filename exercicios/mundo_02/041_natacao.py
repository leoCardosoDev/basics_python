from datetime import date
ano = int(input('Qual ano você nasceu? '))
idade = date.today().year - ano

if idade <= 9:
    print('Você tem {} anos, então você faz parte da categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, então você faz parte da categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, então você faz parte da categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, então você faz parte da categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos, então você faz parte da categoria MASTER'.format(idade))
