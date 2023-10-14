alunos = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar != 'S':
        print(f'{"Noº":<4}{"NOME":<10}{"MEDIA":>8}')
        for pos, linha in enumerate(alunos):
            print(f'{pos:<4}{linha[0]:<10}{linha[2]:>8.1f}')
        while True:
            selecionado = int(
                input('Mostrar notas de qual aluno? (999 interrompe): '))
            if selecionado == 999:
                break
            if 0 <= selecionado < len(alunos):
                print(
                    f'Notas de {alunos[selecionado][0]} são: {alunos[selecionado][1]}')
            else:
                print('Número de aluno inválido. Tente novamente.')
        break
