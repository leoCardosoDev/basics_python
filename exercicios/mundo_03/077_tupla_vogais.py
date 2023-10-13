palavras = ('aprender', 'programar', 'linguagem')

for palavra in palavras:
    a = palavra.lower().find('a')
    e = palavra.lower().find('e')
    i = palavra.lower().find('i')
    o = palavra.lower().find('o')
    u = palavra.lower().find('u')

    print(f'Na palavra {palavra.upper()} temos ', end='')

    # Se a vogal estiver presente, imprima a vogal
    if a != -1:
        print('a ', end='')
    if e != -1:
        print('e ', end='')
    if i != -1:
        print('i ', end='')
    if o != -1:
        print('o ', end='')
    if u != -1:
        print('u ', end='')

    # Se nenhuma vogal estiver presente, imprima 'nenhuma'
    if a == e == i == o == u == -1:
        print('nenhuma')
    else:
        print()
print('-'*40)
print('\n')
print(f'{"Forma corrigida: ":^40}')
print('\n')
print('-'*40)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')
