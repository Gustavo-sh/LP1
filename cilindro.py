import math

print('Cálculo da Superfície de um Cilindro\n---')

diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

print('---')

raio = diametro / 2
areab = math.pi * raio ** 2
areal = 2 * math.pi * raio * altura

areat = (2 * areab) + areal

print('Área calculada: {:.2f}'.format(areat))

# Gustavoas 119210741
# UFCG 2019.2
# Questão cilindro do tst
