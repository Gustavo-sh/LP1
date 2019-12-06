def multiplica_lista(n,lista):
    lista2 = []
    if n == 0:
        return lista2
    for e in range(n):
        for i in lista:
            lista2.append(i)
    return lista2
