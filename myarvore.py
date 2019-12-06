vezes = int(input())
string = ''
poko = 1
poka = vezes
tronco = string + ' ' * (vezes - 1) + 'o'
for e in range(vezes):
    v_o = 'o' * poko
    form = ' ' * (poka - 1)
    string = form + v_o
    print(string)
    poka -= 1
    poko += 2

print(tronco)

# Gustavoas 119210741
# UFCG 2019.2
