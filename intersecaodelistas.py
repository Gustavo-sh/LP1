def meu_in(ref, l2):
    for e in range(len(l2)):
        if l2[e] == ref:
            return True
def cria_iguais(l1, l2):
    aux = []
    for e in range(len(l1)):
        for i in range(len(l2)):
            if l1[e] == l2[i]:
                if not meu_in(l1[e], aux):
                    aux.append(l1[e])
    return aux
def intersecao_listas(l1, l2):
    aux = cria_iguais(l1,l2)
    for e in range(len(l1)):
        l1.pop()
    for i in range(len(aux)):
        l1.append(aux[i])
