def reducoes(lista):
    listar = []
    for e in range(len(lista) - 1):
        sub = lista[e] - lista[e + 1]
        if sub <= 0:
            listar.append(0)
        else:
            listar.append(sub)
    return listar
