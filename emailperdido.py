def meu_in(ref, l):
    for e in range(len(l)):
        if l[e] == ref:
            return True
    return False
def encontra_email_perdido(l1,l2):
    for e in range(len(l1)):
        if not meu_in(l1[e], l2):
            return l1[e]
