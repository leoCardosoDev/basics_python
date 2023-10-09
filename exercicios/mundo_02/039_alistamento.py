from datetime import date
ano = int(input('Qual ano você nasceu? '))
sexo = str(input('''Qual o seu gênero:
[M] - Masculino
[F] - Feminino
[O] - Outros
''')).upper().strip()
idade = date.today().year - ano
if sexo == 'F' or sexo == 'O':
    print('O alistamento não é obrigatório para você! TCHAU!')
    exit()

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você tem {} ano(s)! Ainda faltam {} anos para você se alistar!'.format(idade, 18 - idade))
elif idade > 18:
    print('Você tem {} anos! O seu tempo de alistamento já passou em {} anos!'.format(idade, idade - 18))
else:
    exit()
