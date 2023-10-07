from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} foi um ano BISSEXTO".format(ano))
else:
    print("O ano de {} NÃO foi um ano BISSEXTO".format(ano))
