def remove_divisores_k(l, k, n):
    if len(l) == 0 or n == 0:
        return l
    for e in range(len(l) - 1, -1, -1):
        if k % l[e] == 0:
            l.pop(e)
            n -= 1
        if n == 0: return l
    return l
