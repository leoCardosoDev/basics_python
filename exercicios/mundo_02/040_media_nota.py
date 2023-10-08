nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi de: {:.1f}. Você está reprovado!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de: {:.1f}. Você está de recuperação!'.format(media))
else:
    print(
        'Sua média foi de: {:.1f}. Parabéns! Você foi aprovado!'.format(media))
