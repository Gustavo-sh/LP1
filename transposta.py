def jogar(indice, l):
    lista = []
    for e in range(len(l)):
        lista.append(l[e][indice])
    return lista

def transposta(M):
    listas = []
    for e in range(len(M[0])):
        listas.append(jogar(e, M))
    return listas
