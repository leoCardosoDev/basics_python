reta1 = int(input('Digite o cumprimento de um lado do triângulo: '))
reta2 = int(input('Digite o cumprimento de um outro lado do triângulo: '))
reta3 = int(input('Digite o cumprimento de um outro lado do triângulo: '))

ehUmTriangulo = (reta1 + reta2) > reta3 and (reta2 + reta1) > reta2 and (reta3 + reta2) > reta1
equilatero = reta1 == reta2 and reta2 == reta3 and reta3 == reta1
isosceles = (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta3 == reta1 and reta3 != reta2)

if ehUmTriangulo:
    if equilatero:
        print('É um triângulo Equilatero')
    elif isosceles:
        print('É um triângulo Isosceles')
    else:
        print('É um triângulo Escaleno')
else:
    print('Não é um triângulo')
