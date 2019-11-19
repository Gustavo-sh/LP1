def anula(l):
    pronto = False
    houve = False
    while not pronto:
        for e in range(len(l) - 1, 0, -1):
            if l[e] + l[e - 1] == 0:
                l.pop(e)
                l.pop(e - 1)
                houve = True
                break
        if houve == False:
            pronto = True
        houve = False
