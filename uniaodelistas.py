def meu_in(arg, l):
    for e in range(len(l)):
        if l[e] == arg:
            return True
    return False
def uniao_listas(l1,l2):
    aux = []
    if l1 == []:
        for e in range(len(l2)):
            if not meu_in(l2[e], l1):
                l1.append(l2[e])
        return None
    for e in range(len(l1)):
        if not meu_in(l1[e], aux):
            aux.append(l1[e])
    for e in range(len(l2)):
        for i in range(len(aux)):
            if not meu_in(l2[e], aux):
                aux.append(l2[e])
                break
    print(aux)
    for e in range(len(l1)):
        l1.pop()
    for e in range(len(aux)):
        l1.append(aux[e])
    return None
