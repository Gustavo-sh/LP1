def distribui_materia_prima(l, num):
    indice = 0
    cont = 0
    aux = [[] for e in range(num)]
    for e in range(len(l)):
        for i in range(e, len(l), num):
            aux[indice].append(l[i])
            cont += 1
        indice += 1
        if cont == len(l): break
    return aux
