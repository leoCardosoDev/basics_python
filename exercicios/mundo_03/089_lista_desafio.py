alunos = []
notas = []
media = []
aluno = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas = [nota1, nota2]
    media = [(nota1 + nota2) / 2]
    aluno = [nome, notas, media]
    alunos.append(aluno)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar != 'S':
        print(f'Noº  NOME         MEDIA  ')
        for pos, linha in enumerate(alunos):
            print(f'{pos:} -  {linha[0]} -   {linha[2]}')
        while True:
            selecionado = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            print(f'Notas de {alunos[selecionado][0]} são: {alunos[selecionado][1]}')
            if selecionado == 999:
                break
        break
