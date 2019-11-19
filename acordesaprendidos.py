def meu_in(ref, l):
    for e  in range(len(l)):
        if l[e] == ref:
            return True
    return False
def acordes(m1, m2):
    aux = []
    for e in range(len(m1)):
        if not meu_in(m1[e], aux):
            aux.append(m1[e])
    for e in range(len(m2)):
        if not meu_in(m2[e], aux):
            aux.append(m2[e])
    return aux
