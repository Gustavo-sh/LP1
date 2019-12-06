def maioridade_penal(str1,str2):
    lista = []
    strin1 = str1.split()
    strin2 = str2.split()
    string = ''
    for e in range(len(strin2)):
        if int(strin2[e]) >= 18:
            lista.append(strin1[e])
    if lista == []:
        return string
    if len(lista) == 1:
        return lista[0]
    for e in range(len(lista)):
        if e == len(lista) - 1:
            string += lista[e]
            return string
        string += lista[e] + ' '
