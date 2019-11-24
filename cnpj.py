cnpj = input()

dig1 = int(cnpj[0])
dig2 = int(cnpj[1])
dig3 = int(cnpj[3])
dig4 = int(cnpj[4])
dig5 = int(cnpj[5])
dig6 = int(cnpj[7])
dig7 = int(cnpj[8])
dig8 = int(cnpj[9])
matrix = '0001'
dig9 = int(matrix[0])
dig10 = int(matrix[1])
dig11 = int(matrix[2])
dig12 = int(matrix[3])

soma = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9 + dig10 + dig11 + dig12

print('{}/{}-{:02d}'.format(cnpj, matrix, soma))

# Gustavoas 119210741
# UFCG 2019.2
# cnpj do TST
