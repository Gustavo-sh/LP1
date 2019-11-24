import string

palavra = list(input())
indice_a = 1
indice_e = 1
indice_i = 1
indice_o = 1
troca_a = 0
troca_e = 0
troca_i = 0
troca_o = 0

for e in range(len(palavra) - 1):
    if palavra[indice_a] == 'a' or palavra[indice_a] == 'A':
        palavra[indice_a] = '4'
        troca_a += 1
    indice_a += 1

for e in range(len(palavra) - 1):
    if palavra[indice_e] == 'e' or palavra[indice_e] == 'E':
        palavra[indice_e] = '3'
        troca_e += 1
    indice_e += 1

for e in range(len(palavra) - 1):
    if palavra[indice_i] == 'i' or palavra[indice_i] == 'I':
        palavra[indice_i] = '1'
        troca_i += 1
    indice_i += 1

for e in range(len(palavra) - 1):
    if palavra[indice_o] == 'o' or palavra[indice_o] == 'O':
        palavra[indice_o] = '0'
        troca_o += 1
    indice_o += 1

trocas = troca_a + troca_e + troca_i + troca_o
new = ''.join(palavra)
print('{} ({} troca(s))'.format(new, trocas))

# Gustavoas119210741
# UFCG 2019.2
