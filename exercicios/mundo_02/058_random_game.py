from random import randint
pc = randint(0, 10)
cont = 0
user = int(input('Adivinha um numero de 0 a 10: '))
while user != pc:
  cont+=1
  user = int(input('Você errou! Tenta de novo [ 0 até 10]: '))
print(f'Você precisou de {cont} para adivinhar o número = {pc}')
