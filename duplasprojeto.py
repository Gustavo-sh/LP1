def meu_in(ref, l):
    for e in range(len(l)):
        if l[e] == ref:
            return True
    return False
def insere_nome(a1, duplas, a2):
    if not meu_in(a2, duplas):
        duplas.append(a1)
        return None
    duplas.append(a1)
    for e in range(len(duplas) - 1, -1, -1):
        duplas[e], duplas[e - 1] = duplas[e - 1], duplas[e]
        if duplas[e] == a2: break
