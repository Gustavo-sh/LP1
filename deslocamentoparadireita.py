def desloca(l, n1, n2):
    for e in range(n1, n2):
        l[e], l[e + 1] = l[e + 1], l[e]
        if e + 1 == n2: break
