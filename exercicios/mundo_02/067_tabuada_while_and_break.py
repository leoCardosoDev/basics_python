multiplicador = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while multiplicador <= 10:
        print(f'{n:>2} x {multiplicador:>2} = {n * multiplicador:>2}')
        multiplicador += 1
    multiplicador = 0
