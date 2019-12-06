def verifica_esteira(l1,l2):
    for e in range(len(l1)):
        for i in range(len(l2)):
            if l1[e] == l2[i]:
                if i > e:
                    return False
    return True
