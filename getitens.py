def get_items(valores, indices):
    lista = []
    for e in range(len(indices)):
        if indices[e] >= len(valores):
            lista.append(None)
        else:
            lista.append(valores[indices[e]])
    return lista
