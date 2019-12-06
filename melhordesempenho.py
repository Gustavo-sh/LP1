vezes = int(input())
lista = []
quants = 0
maior = 0
aluno = 0

for e in range(vezes):
    reg = input()
    for i in range(len(reg)):
        if reg[i] == '.':
            quants += 1
    if quants != 0:
        lista.append(quants)
        lista.append(e + 1)
    quants = 0

if lista != []:
    for e in range(0, len(lista), 2):
        if lista[e] > maior:
            maior = lista[e]
            aluno = lista[e + 1]

    print(aluno)
else:
    print('-1')
