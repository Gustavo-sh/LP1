seq = input()
soma1 = 0
soma2 = 0

for e in range(0, 5, 2):
    soma1 += int(seq[e])
for e in range(1, 5, 2):
    soma2 += int(seq[e])

produto = soma1 * soma2

produto = soma1 * soma2

print('{:05d}'.format(produto))
