def filtra_altera_lista(num, l):
    for e in range(len(l) - 1, -1, -1):
        if str(abs(e)/num)[2] != '0':
            l.pop(e)

lista1 = [0,1,2,3,4,5,6]
filtra_altera_lista(2, lista1)
assert lista1 == [0,2,4,6]
filtra_altera_lista(3, lista1)
assert lista1 == [0,6]
