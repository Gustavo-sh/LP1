def resto_da_maior(capacity, t, aux, guardar):
    i = 0
    for e in range(guardar + 1, len(t)):
        aux[i].append(t[e])
        if len(aux[i]) == capacity:
            i = 1

def principal(t1, t2, capacity, aux):
    quant = 0
    indice = 0
    guardar = 0
    menor = 0
    if len(t1) < len(t2):
        menor = t1
    else:
        menor = t2
    for e in range(len(menor)):
        aux[indice].append(t1[e])
        quant += 1
        if len(aux[0]) == capacity: indice = 1
        aux[indice].append(t2[e])
        quant += 1
        if len(aux[0]) == capacity: indice = 1
        guardar = e
    return [guardar, quant]

def distribui_alunos(t1, t2, capacity):
    aux = [[], []]
    soma = len(t1) + len(t2)
    funtion = principal(t1, t2, capacity, aux)
    guardar = funtion[0]
    quant = funtion[1]
    if quant < soma:
        if len(aux[0]) < capacity:
            if len(t1) > len(t2):
                resto_da_maior(capacity, t1, aux, guardar)
            else:
                resto_da_maior(capacity, t2, aux, guardar)
        else:
            if len(t1) > len(t2):
                for e in range(guardar + 1, len(t1)):
                    aux[1].append(t1[e])
            else:
                for e in range(guardar + 1, len(t2)):
                    aux[1].append(t2[e])
    return aux
