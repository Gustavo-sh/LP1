def conta_votos(listas, num):
    sim = 0
    nao = 0
    lista = []
    for e in range(len(listas)):
        normal = listas[e].split(',')
        if int(normal[1]) == num:
            if normal[4] == 'sim':
                sim += 1
            else:
                nao += 1
    lista.append(sim)
    lista.append(nao)
    return lista
