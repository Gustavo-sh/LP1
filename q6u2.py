n = input()

d1 = int(n[0])
d2 = int(n[1])
d3 = int(n[2])
d4 = int(n[3])
d5 = int(n[4])

soma = d1 + d2 + d3 + d4 + d5

r = soma % 11

print('{}-{:02d}'.format(n, r))

