extenso = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
num = int(input('Digite um número de 0 a 20: '))

if num > 20 or num < 0:
    while True:
        num = int(input('Tente novamente! Digite um número de 0 a 20: '))
        if num <= 20 or num >= 0:
            break
print(f'Você digitou {extenso[num]}')
