palavra = input()
lista_vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
cont = 0

for e in palavra:
    for i in range(len(lista_vogais)):
        if e == lista_vogais[i]:
            print(e)
            cont += 1
            break
    if cont == 1:
        break
if cont == 0:
    print('-')
