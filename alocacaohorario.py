def my_in(ref, l):
    for e in range(len(l)):
        if l[e] == ref:
            return True
    return False
def get_choque_horario(l):
    aux = []
    for e in range(len(l)):
        for i in range(len(l)):
            if l[e][-1] == l[i][-1] and e != i:
                if not my_in(l[e], aux):
                    aux.append(l[e])
                if not my_in(l[i], aux):
                    aux.append(l[i])
    return aux
