def remove_consecutivas(l):
    aux = []
    controle = False
    for e in range(len(l)):
        for i in range(len(l[e]) - 1):
            if l[e][i] == l[e][i + 1]:
                controle = True
                break
            elif l[e][i] == chr(ord('A') + ord(l[e][i + 1]) - ord('a')):
                controle = True
                break
            elif chr(ord('A') + ord(l[e][i]) - ord('a')) == l[e][i + 1]:
                controle = True
                break
        if controle == False:
            aux.append(l[e])
        controle = False
    for e in range(len(l)):
        l.pop()
    for e in range(len(aux)):
        l.append(aux[e])
