safra = int(input())
c_atacado = int(input())
c_varejo = int(input())

atacado = int(safra / c_atacado)
varejo = float((safra % c_atacado)) / c_varejo

# print('{:.2f}'.format(varejo))

print('Clientes no atacado = {}kg cada.\nClientes no varejo = {:.2f}kg cada.'.format(atacado, varejo))
