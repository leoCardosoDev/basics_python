valores = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num >= max(valores):
        valores.append(num)
        print('Adicionado ao final da lista')
    elif num <= min(valores):
        valores.insert(0, num)
        print(f'Valor adicionado na posição 0 da lista')
    elif num >= valores[0]:
        valores.insert(1, num)
        print(f'Valor adicionado na posição 1 da lista')
    elif num >= valores[1]:
        valores.insert(2, num)
        print(f'Valor adicionado na posição 3 da lista')
    elif num >= valores[2]:
        valores.insert(3, num)
        print(f'Valor adicionado na posição 2 da lista')

print(f'Os valores digitados em ordem foram: {valores}')
# melhora a lógica com while
