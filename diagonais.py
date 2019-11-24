def diagonais(ll):
    lista = [[], []]
    indice = -1
    for e in range(len(ll)):
        lista[0].append(ll[e][e])
        lista[1].append(ll[e][indice])
        indice -= 1
    return lista
