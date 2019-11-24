def colegas_de_sala(dic, ref):
    lista = []
    for e in dic.items():
        if e[0] != ref and e[1] == dic[ref]:
            lista.append(e[0])
    return lista
