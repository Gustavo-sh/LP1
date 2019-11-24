quant = int(input())
tot = [quant]
soma = quant

for i in range(len(tot), 7):
    quant = int(input())
    tot.append(quant)
    soma += quant

media = (tot[0] + tot[1] + tot[2] + tot[3] + tot[4] + tot[5] + tot[6]) / 7

print('Total: {}'.format(soma))
print('Média: {:.2f}'.format(media))

# Gustavoas 119210741
# UFCG 2019.2
# Questão callcenter do tst
