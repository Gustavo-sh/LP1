a = int(input())
b = int(input())
c = int(input())

d = bool(abs(b - c) < a < b + c)
e = bool(abs(a - c) < b < a + c)
f = bool(abs(a - b) < c < a + b)

soma = a + b + c

if d == True and e == True and f == True:
    print('triangulo valido. {}'.format(soma))

else:
    print('triangulo invalido.')

# Gustavoas 119210741
# UFCG 2019.2
# Questão etriangulo do tst
