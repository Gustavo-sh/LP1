b2 = input()
lista = []
lista_indices = []
soma = 0
indice = 1
indice2 = 1
for e in range(len(b2) - 1, -1, -1):
  num = int(b2[e]) * indice2
  lista.append(num)
  lista_indices.append(indice2)
  indice2 = indice2 * 2
indice2 = 0
for e in range(len(lista) - 1, -1, -1):
  print('{} * {} = {}'.format(b2[indice2], lista_indices[e], lista[e]))
  soma += int(lista[e])
  indice2 += 1
print('{}(2) = {}(10)'.format(b2, soma))
