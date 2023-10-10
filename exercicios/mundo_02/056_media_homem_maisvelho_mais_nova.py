def obter_dados_pessoa():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('''Digite o seu sexo:
      [M] = Masculino
      [F] = Feminino
    ''').strip().upper()
    return {"nome": nome, "idade": idade, "sexo": sexo}

pessoas = []
for _ in range(4):
    pessoa = obter_dados_pessoa()
    pessoas.append(pessoa)

idades = [pessoa["idade"] for pessoa in pessoas]
sexos = [pessoa["sexo"] for pessoa in pessoas]

# Calcular média
media = sum(idades) / len(idades)
print(f'A média de idade do grupo é de {media:.1f}')

# Encontrar homem mais velho
homem_mais_velho = max(pessoas, key=lambda pessoa: pessoa["idade"])
print(f'O homem mais velho é {homem_mais_velho["nome"]} com {homem_mais_velho["idade"]} anos.')

# Contar mulheres com menos de 20 anos
mulheres_menos_20 = sum(1 for pessoa in pessoas if pessoa["sexo"] == 'F' and pessoa["idade"] < 20)
print(f'Número de mulheres com menos de 20 anos: {mulheres_menos_20}')
