def split(frase, delimitador):
    string = ''
    lista = []
    a = '['', '']'
    if delimitador == frase:
        return a
    for e in range(len(frase)):
        if frase[e] != delimitador:
            string += frase[e]
        else:
            if string != '':
                lista.append(string)
                string = ''
        if e == len(frase) - 1:
            if string != '':
                lista.append(string)
            return lista
