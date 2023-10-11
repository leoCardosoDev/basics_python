num = 0
cont = 0
result = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        result += num
        cont += 1
print(f'Você digitou {cont} e a soma entre eles foi de {result}')
