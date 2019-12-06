reprovados = 0
cont = 0

while True:
    aluno = input()
    cont = 0
    if aluno == '-': break
    for e in range(len(aluno)):
        if aluno[e] == 'f':
            cont += 1
        if cont == 9:
            reprovados += 1
            cont = 0
            break

print('{} aluno(s) reprovado(s) por falta.'.format(reprovados))
