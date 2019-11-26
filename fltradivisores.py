def filtra_divisores(l):
    for e in range(len(l) - 1, -1, -1):
        el = str(l[e])
        lo = 0
        for i in el:
            lo += int(i)
        if l[e] % lo != 0:
            l.pop(e)
        lo = 0
