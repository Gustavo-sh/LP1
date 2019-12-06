def quanto_tempo(h1, h2):
    t1 = h1.split(':')
    t2 = h2.split(':')
    obs2 = int(t2[1])
    obs1 = int(t1[1])
    dif1 = int(t2[0]) - int(t1[0])
    if obs2 < obs1:
        dif1 -= 1
        dif2 = 60 - abs(int(t2[1]) - int(t1[1]))
    else:
        dif2 = int(t2[1]) - int(t1[1])
    resp = '{} hora(s) e {} minuto(s)'.format(dif1, dif2)
    return resp
