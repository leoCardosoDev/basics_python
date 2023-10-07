sa = int(input('Qual é o seu sálario atual? R$: '))
if sa >= 1250:
    dp = (10 / 100) * sa
    print('Seu salário de R$ {:.2f} recebeu um aumento de 10% e agora você receberá R$ {:0.2f}'.format(sa, sa+dp))
else:
    dp = (15 / 100) * sa
    print('Seu salário de R$ {:.2f} recebeu um aumento de 15% e agora você receberá R$ {:0.2f}'.format(sa, sa+dp))
