palavra1 = input()
palavra2 = input()
cont = 0
total = len(palavra1) + len(palavra2)
defi = 0

if palavra1 > palavra2:
    defi = palavra2
else:
    defi = palavra1

print('Letras coincidentes')

for e in range(len(defi)):
    if palavra1[e] == palavra2[e]:
        print("'{}' na posição {}".format(palavra1[e], e + 1))
        cont += 1

print('Total de letras coincidentes: {} ({}%)'.format(cont, int((cont/total) * 100)))
