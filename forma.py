palavras = [input() for palavra in range(3)]

tamanho_palavra = len(palavras[0])
palavra = []
maior = ''

for i in range(tamanho_palavra):
  a = palavras[0][i]
  b = palavras[1][i]
  c = palavras[2][i]

  for v in range(1):
    if a > b:
      if a > c:
        maior = a
      else:
        maior = c
    elif b > c:
      maior = b
    else:
      maior = c
  palavra.append(maior)

print(''.join(palavra))
