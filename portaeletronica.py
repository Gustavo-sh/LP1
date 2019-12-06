letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
lista = []
printar = 0

while True:
    op = input()
    if op == 'S': break
    top = op.split()
    if top[0] == 'R':
        for e in range(len(letras)):
            if top[1][0] == letras[e]:
                lista.append(letras[e])
                lista.append(1)
    if top[0] == 'P':
        for e in range(0, len(lista), 2):
            if lista[e] == top[1][0]:
                printar += 1
        print(printar)
    printar = 0
