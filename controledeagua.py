import math

vel_vazao = float(input())
dia_cano = float(input())
tempo = float(input())

secao = math.pi * (dia_cano / 2) ** 2
vazao = vel_vazao * secao * 1000
quant_agua = tempo * vazao

print('Quantidade de água = {:.2f} litros.'.format(quant_agua))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 24 do TST
