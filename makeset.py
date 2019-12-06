def meu_in(arg, l):
    for e in range(len(l)):
        if arg == l[e]:
            return True
    return False

def make_set(l):
    clint = []
    for e in range(len(l)):
        if not meu_in(l[e], clint):
            clint.append(l[e])
    for e in range(len(l)):
        l.pop()
    for e in range(len(clint)):
        l.append(clint[e])
