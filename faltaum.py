def encontra_rotulo_perdido(l1,l2):
    string = ''
    cont = 0
    for e in range(len(l1)):
        for i in range(len(l2)):
            if l1[e] == l2[i]:
                cont += 1
        if cont == 0:
            string += l1[e]
        cont = 0
    return string
