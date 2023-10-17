def leiaDinheiro(mensagem):
  dinheiro = input(mensagem)

  while dinheiro.isalnum() or dinheiro.isalpha or dinheiro.isspace():
    if dinheiro.isnumeric():
      break
    print(f'\033[1;31mERRO! "{dinheiro}" é um preço inválido\033[m')
    dinheiro = input(mensagem)
  return float(dinheiro)
