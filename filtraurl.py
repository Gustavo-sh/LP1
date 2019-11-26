def isp(obj, item):
    string = ''
    aux = []
    for e in range(len(item)):
        if item[e] == obj:
            aux.append(string)
            string = ''
        else:
            string += item[e]
        if e == len(item) - 1:
            aux.append(string)
    return aux
def filtra_urls(l):
    aux = []
    for e in range(len(l)):
        algo = isp('.', l[e])
        for i in range(len(algo)):
            if algo[i] == 'google':
                aux.append(l[e])
                break
    return aux
