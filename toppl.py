def meu_in(ref, l):
    for e in range(len(l)):
        if l[e] == ref:
            return True
    return False
def filtra_alunos(l1, l2, media):
    cont = 0
    for e in range(len(l1) - 1, -1, -1):
        if not meu_in(l1[e][0], l2) or l1[e][1] < media:
            l1.pop(e)
            cont += 1
    return cont
