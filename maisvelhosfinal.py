def maiores_final(l):
    indice = -1
    for e in range(len(l) - 1, -1, -1):
        if l[e] >= 18:
            l[e], l[indice] = l[indice], l[e]
            indice -= 1
