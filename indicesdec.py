frase = input()
chave = input()
ocorrencia = 0
lista = []

for letra in chave:
    for e in range(len(frase)):
        if letra == frase[e]:
            ocorrencia += 1
            lista.append(str(e))
            
    if len(lista) != 0:
        print('{}'.format(' '.join(lista))) 
    if ocorrencia == 0:
        print('-1')
    ocorrencia = 0
    lista = []

# Gustavoas 119210741
# UFCG 2019.2
