frase = input()
chave = input()
string = ''

for e in range(len(frase)):
    if frase[e] == str(e):
        string += chave[e]
    if frase[e] != str(e):
        string += frase[e]

print(string)

# Gustavoas 119210741
# UFCG 2019.2
