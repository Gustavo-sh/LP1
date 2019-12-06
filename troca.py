frase = input()
chave = input()
string = ''

for e in range(len(frase)):
    for i in range(10):
        if frase[e] == str(i):
            string += chave[i]
            break
    if frase[e] != str(i):
        string += frase[e]

print(string)

# Gustavoas 119210741
# UFCG 2019.2
