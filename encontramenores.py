def encontra_menores(num, lista):
    for e in lista:
        if e < num:
            return e
    return -1
