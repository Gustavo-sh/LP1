abstencoes = int(input())
v_a_favor = int(input())
v_contra = int(input())

total = abstencoes + v_a_favor + v_contra

p_abstencoes = (abstencoes / total) * 100
p_v_a_favor = (v_a_favor / total) * 100
p_v_contra = (v_contra / total) * 100

print('Resultado da Votação')

print('')

print('{} abstenções ({:.2f}%)'.format(abstencoes, p_abstencoes))
print('{} a favor ({:.2f}%)'.format(v_a_favor, p_v_a_favor))
print('{} contra ({:.2f}%)'.format(v_contra, p_v_contra))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 30 do TST
# Arigato
