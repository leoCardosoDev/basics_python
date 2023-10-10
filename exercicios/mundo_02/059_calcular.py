num1 = int(input('Digite um 1º número: '))
num2 = int(input('Digite um 2º número: '))
operacao = 0
while operacao != 5:
    operacao = int(input('''O que você quer fazer:
      [1] Somar
      [2] Multiplicar
      [3] Maior - menor
      [4] Novos números
      [5] Sair
 '''))
    if operacao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif operacao == 3:
        if num2 > num1:
            print(f'O número {num2} é MAIOR que {num1}')
        else:
            print(f'O número {num1} é MAIOR que {num2}')
    elif operacao == 4:
        num1 = int(input('Digite novo 1º número: '))
        num2 = int(input('Digite novo 2º número: '))
print('FIM')
