frase = input()
num1 = int(input())
num2 = int(input())
string = ''

if frase[num1] != ' ':
    string += frase[num1]
else:
    string += ' ,'

for e in range(num1 + 1, num2, 1):
    if frase[e] != ' ':
        string += (' ' + frase[e])
    else:
        string += ' ,'

print(string)

# Gustavoas 119210741
# UFCG 2019.2
