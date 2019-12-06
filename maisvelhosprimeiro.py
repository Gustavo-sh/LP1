def idosos_inicio(fila):
    indice = 0
    for e in range(len(fila)):
        if fila[e] >= 60:
            fila[indice], fila[e] = fila[e], fila[indice]
            indice += 1
