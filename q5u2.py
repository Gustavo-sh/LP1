import math

raio = float(input())

areac = math.pi * raio ** 2

ladoq = (((raio * 2) ** 2) / 2) ** 0.5

areaq = ladoq * ladoq

areanq = areac - areaq

print('Área não comum: {:.5f}'.format(areanq))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 4u2 do TST
    # Arigato
