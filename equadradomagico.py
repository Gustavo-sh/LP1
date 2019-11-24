def unidimension(ref, l):
    cont = 0
    for e in range(len(l)):
        if l[e] == ref:
            cont += 1
    if cont == 1 or cont == 0:
        return True
    else:
        return False

def soma(l):
    soma = 0
    for e in range(len(l)):
        soma += l[e]
    return soma

def eh_quadrado_magico(l):
    unic = soma(l[0])
    somar = 0
    indice = 0
    for e in range(len(l)):
        for i in range(len(l)):
            if not unidimension(l[i][indice], l[i]):
                return False
            somar += l[i][indice]
        if somar != unic:
            return False
        else:
            somar = 0
        indice += 1
    
    for e in range(len(l)):
        if soma(l[e]) != unic:
            return False
    
    somate1 = 0
    somate2 = 0
    indice = -1
    for e in range(len(l)):
        somate1 += l[e][e]
        somate2 += l[e][indice]
        indice -= 1
    if somate1 != unic or somate2 != unic:
        return False

    return True
