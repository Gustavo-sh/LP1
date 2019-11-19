def ajeita_lista(l):
    indice = 0
    for e in range(len(l)):
        if l[e] % 2 == 0:
            l[e], l[indice] = l[indice], l[e]
            indice += 1
    for e in range(indice):
        for i in range(indice):
            if l[i] < l[e]:
                l[e], l[i] = l[i], l[e]
    for e in range(indice, len(l)):
        for i in range(indice, len(l)):
            if l[i] > l[e]:
                l[e], l[i] = l[i], l[e]
