def meu_in(arg, l):
    for e in range(len(l)):
        if l[e] == arg:
            return True
    return False
def get_frequencia(l):
    aux = []
    sub_aux = []
    var = 0
    for e in range(len(l)):
        if not meu_in(l[e], sub_aux):
            sub_aux.append(l[e])
            for i in range(len(l)):
                if l[e] == l[i]:
                    var += 1
            sub_aux.append(var)
            var = 0
    for e in range(1, len(sub_aux), 2):
        aux.append(sub_aux[e])
    return aux
