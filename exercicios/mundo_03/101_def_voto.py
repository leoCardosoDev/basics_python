def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade > 15 and idade <= 17 or idade > 65:
        print(f'Com {idade} anos: Seu VOTO É OPCIONAL')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos: Seu VOTO É OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')


ano = int(input('Digite o ano do seu nascimento: '))
voto(ano)
