def conta_votos(lista, ide):
    sim = 0
    nao = 0
    mostrar = []
    for e in range(len(lista)):
        olhar = lista[e].split(',')
        if int(olhar[2]) == ide:
            if olhar[1] == 'sim':
                sim += 1
            else:
                nao += 1
    mostrar.append(sim)
    mostrar.append(nao)
    return mostrar
