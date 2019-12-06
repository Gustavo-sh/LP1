def meu_in(ref, l):
    indice = 1
    cont = 1
    for e in range(len(l)):
        if l[e] == ref[0]:
            if len(ref) - 1 > len(l) - (e + 1):
                        return False
            for i in range(1, len(ref)):
                if l[e + indice] != ref[i]:
                    if len(ref) - 1 > len(l) - (e + 1):
                        return False
                    else:
                        cont = 1
                        break
                else:
                    cont += 1
                if cont == len(ref):
                    return True
                indice += 1
    return False
def is_substring(s1, s2):
    if len(s1) < len(s2):
        return False
    if len(s1) == len(s2):
        for e in range(len(s1)):
            if s1[e] != s2[e]:
                return False
        return True
    if len(s2) == 1:
        for e in range(len(s1)):
            if s1[e] == s2[0]:
                return True
    return meu_in(s2, s1)
