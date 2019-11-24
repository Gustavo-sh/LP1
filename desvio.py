a = input().split()
b = input().split()
soma1 = 0
media1 = 0
soma2 = 0
media2 = 0
sub1 = 0
sub2 = 0
n1 = len(a) - 1
n2 = len(b) - 1

for e in range(len(a)):
    soma1 += float(a[e])

media1 = soma1 / len(a)

for e in range(len(b)):
    soma2 += float(b[e])

media2 = soma2 / len(b)

for e in range(len(a)):
    c = (float(a[e]) - media1) ** 2
    sub1 += c

for e in range(len(b)):
    d = (float(b[e]) - media2) ** 2
    sub2 += d

desv1 = (sub1 / n1) ** 0.5
desv2 = (sub2 / n2) ** 0.5

if desv1 > desv2:
    print('A sequência 1 possui o maior desvio padrão ({:.2f}).'.format(desv1))
elif desv2 > desv1:
    print('A sequência 2 possui o maior desvio padrão ({:.2f}).'.format(desv2))
else:
    print('As sequências possuem o mesmo desvio padrão ({:.2f}).'.format(desv1))
