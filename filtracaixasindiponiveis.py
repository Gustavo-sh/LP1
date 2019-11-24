def filtra_caixas_indisponiveis(l,num):
    for e in range(len(l) - 1, -1, -1,):
        if l[e] < num:
            l.pop(e)
