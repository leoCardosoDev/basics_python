n = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
while n != 0:
    print(f'{a} -> ', end='')
    c = a + b
    a = b
    b = c
    n -= 1

# Proposta Guanabara
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
