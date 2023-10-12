cedulas1 = 0
cedulas10 = 0
cedulas20 = 0
cedulas50 = 0
saque = float(input('Que valor você quer sacar? R$ '))
while True:
    if saque <= 0:
        break
    if saque >= 50:
        cedulas50 = int(saque / 50)
        saque -= 50 * cedulas50
        print(f'Total de {cedulas50} cédulas de R$ 50')
    if saque >= 20:
        cedulas20 = int(saque / 20)
        saque -= 20 * cedulas20
        print(f'Total de {cedulas20} cédulas de R$ 20')
    if saque >= 10:
        cedulas10 = int(saque / 10)
        saque -= 10 * cedulas10
        print(f'Total de {cedulas10} cédulas de R$ 10')
    if saque >= 1:
        cedulas1 = int(saque)
        saque -= 1 * cedulas1
        print(f'Total de {cedulas1} cédulas de R$ 1')
