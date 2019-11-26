def inverte3a3(s):
    indice = 0
    string = ''
    aux =[]
    for e in range(len(s)):
        string += s[e]
        indice += 1
        if indice == 3:
            aux.append(string)
            indice = 0
            string = ''
    string = ''
    for e in range(len(aux) - 1, -1, -1):
        string += aux[e]
    return string
