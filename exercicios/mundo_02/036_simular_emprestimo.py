valorDaCasa = float(input('Qual o valor da casa? R$: '))
salarioComprador = float(input('Qual é o salário do comprador? R$: '))
qtdAnos = int(input('Em quantos anos pretende pagar? '))
parcelas = valorDaCasa / (qtdAnos * 12)

if parcelas > salarioComprador - (30 / 100) * salarioComprador:
  print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}\n EMPRESTIMO NEGADO! '.format(valorDaCasa, qtdAnos, parcelas))
else:
  print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}\n EMPRESTIMO APROVADO! '.format(valorDaCasa, qtdAnos, parcelas))
