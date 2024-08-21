def leitura():
    total = 0
    while True:
        faltas = 0
        alunos = input()
        if alunos == '-': break
        i = 0
        while i < len(alunos):
            if alunos[i] == 'f':
                faltas += 1
            if faltas > 8:
                total += 1
                break
            i += 1
    print(f'{total} aluno(s) reprovado(s) por falta.')

leitura()
