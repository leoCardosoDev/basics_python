for c in range(1, 10):
    print(c, end='- ')
print('FIM')

c = 1
while c < 10:
    print(c, end='- ')
    c += 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    v = str(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

nu = 1
par = impar = 0
while nu != 0:
    nu = int(input('Digite um valor: '))
    if n != 0:
        if nu % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')
