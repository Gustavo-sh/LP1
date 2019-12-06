def sei_tocar_musica(m, a):
    very = 0
    for e in range(len(m)):
        for i in range(len(a)):
            if a[i] == m[e]:
                very += 1
        if very == 0:
            return False
        very = 0
    return True
