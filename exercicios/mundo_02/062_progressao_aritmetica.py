primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = 10
decimo = primeiro + (termos - 1) * razao
adicional = 1

c = primeiro
while c <= decimo and adicional != 0:
    print(f'{c}', end=' -> ')
    c += razao
    if decimo < c:
        print(' PAUSA ')
        adicional = int(input('Quantos termos você quer mostrar a mais: '))
        decimo = c + (adicional - 1) * razao
        termos += adicional
print(f'Progressão finalizada com {termos} termos mostrados')
