def soma_diminui_vizinhos(lista):
    if lista == []:
        return 0
    if len(lista) == 1:
        return lista[0]
    alvo = lista[0] + lista[1]
    for e in range(2, len(lista)):
        if e % 2 == 1:
            alvo += lista[e]
        else:
            alvo -= lista[e]
    return alvo
