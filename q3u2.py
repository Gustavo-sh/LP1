import math

ladoq = float(input())

raioq = (ladoq ** 2 + ladoq ** 2) ** 0.5
perimetro = raioq * math.pi

print('Perímetro: {:.5f}'.format(perimetro))

area = (raioq / 2) ** 2 * math.pi

print('Área: {:.5f}'.format(area))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 3u2 so TST
# Arigato
