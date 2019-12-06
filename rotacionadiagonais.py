def rotaciona_ds(m, lado):
    indice = -1
    indice2 = 0
    if lado == 'cima':
        for e in range(len(m) - 1):
            m[e][indice], m[e + 1][indice - 1] = m[e + 1][indice - 1], m[e][indice]
            indice -= 1
    else:
        for e in range(len(m) - 1, 0, -1):
            m[e][indice2], m[e - 1][indice2 + 1] = m[e - 1][indice2 + 1], m[e][indice2]
            indice2 += 1
