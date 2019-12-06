vezes = int(input())
dobradas = []
nao_dobradas = []
cont1 = 0
cont2 = 0

for e in range(vezes):
    palavra = input()

    for e in range(len(palavra) - 1):
        if palavra[e] == palavra[e + 1]:
            cont1 += 1
            dobradas.append(palavra)
            break

    if cont1 == 0:
        nao_dobradas.append(palavra)
    else:
        cont1 -= 1

print('{} palavra(s) com letras dobradas:'.format(len(dobradas)))
for e in dobradas:
    print(e)

print('---')

print('{} palavra(s) sem letras dobradas:'.format(len(nao_dobradas)))
for e in nao_dobradas:
    print(e)

# Gustavoas 119201741
# UFCG 2019.2
