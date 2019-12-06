refe = int(input())
soma = 0
for e in range(10):
    num = int(input())
    rest = num % refe
    if rest == 0:
        soma += num

print(soma)

# Gustavoas 119210741
# UFCG 2019.2
