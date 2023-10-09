peso = float(input('Qual o seu peso? Kg: '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso com {:.2f} de Indice de massa corporal'.format(imc))
elif imc < 25:
    print(
        'Você está no peso ideal com {:.2f} de Indice de massa corporal'.format(imc))
elif imc < 30:
    print(
        'Você está com sobrepeso com {:.2f} de Indice de massa corporal'.format(imc))
elif imc < 40:
    print(
        'Você está com obesidade grau II com {:.2f} de Indice de massa corporal'.format(imc))
else:
    print(
        'Você está com obesidade grau III com {:.2f} de Indice de massa corporal'.format(imc))
