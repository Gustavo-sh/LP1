def acha_m(lista):
    maior = lista[0]
    for e in range(len(lista)):
        if lista[e] > maior:
            maior = lista[e]
    return maior
def top_3(lista):
    maior = acha_m(lista)
    lista2 = []
    lista3 = []
    for e in range(len(lista)):
        if lista[e] == maior:
            lista[0], lista[e] = lista[e], lista[0]
    for e in range(1, len(lista)):
        lista2.append(lista[e])
    maior = acha_m(lista2)
    for e in range(len(lista)):
        if lista[e] == maior:
            lista[1], lista[e] = lista[e], lista[1]
    for e in range(2, len(lista)):
        lista3.append(lista[e])
    maior = acha_m(lista3)
    for e in range(len(lista)):
        if lista[e] == maior:
            lista[2], lista[e] = lista[e], lista[2]
