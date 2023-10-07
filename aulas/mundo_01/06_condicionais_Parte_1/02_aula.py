n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2

if m >= 6.0:
    print('Sua média foi de {:.1f}. Parabéns! Voce passou!'.format(m))
else:
    print(
        'Sua média foi de {:.1f}. Hummm... você ficou de recuperação'.format(m))
