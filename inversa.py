palavra = input()
lista = []
cont = 0

for e in range(len(palavra) - 1, -1, -1):
  lista.append(palavra[e])

for e in range(len(palavra)):
    if palavra[e] == lista[e]:
        cont += 1

print('A palavra {} contém {} caractere(s) coincidente(s) com a sua inversa.'.format(palavra, cont)) 
