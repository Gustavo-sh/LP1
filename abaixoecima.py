def organiza_por_media(l):
    soma = 0
    contar = 0
    indice = 0
    ordenado = False
    control = False
    if len(l) == 0:
        return []
    for e in range(len(l)):
        soma += l[e]
        contar += 1
    media = soma / contar
    while not ordenado:
        for e in range(len(l) - 1):
            if l[e] > media:
                for i in range(e + 1, len(l)):
                    if l[i] > media:
                        indice = 0
                        break
                    l[i], l[e + indice] = l[e + indice], l[i]
                    indice += 1
                    control = True
        if control == False: break
        control = False
    return l
