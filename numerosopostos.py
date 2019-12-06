def lista_so_com_oposto(l):
    cont = 0
    op = 0
    for e in range(len(l) - 1, -1, -1):
        op = -l[e]
        for i in range(len(l)):
            if l[i] == op:
                cont += 1
        if cont == 0:
            l.pop(e)
        cont = 0
