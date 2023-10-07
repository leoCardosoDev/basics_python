km = int(input('Qual velocidade o carro passou aqui: '))
ltd = 80
if km > ltd:
  multa = (km - ltd) * 7.00
  print('Você excedeu o limite de velocidade de {}km/h ao atingir {}km/h terá que pagar uma multa de R$: {}'.format(ltd, km, multa))
