ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print("{} foi um ano BISSEXTO".format(ano))
else:
    print("{} NÃO foi um ano BISSEXTO".format(ano))
