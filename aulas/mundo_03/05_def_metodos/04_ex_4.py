def dobra(lts):
  pos = 0
  while pos < len(lts):
    lts[pos] *= 2
    pos+=1

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
