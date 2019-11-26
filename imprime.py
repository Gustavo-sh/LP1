n = int(input())
times = []
pontos = []
pos = 1

for i in range(n):
    times.append(input())
    pontos.append(input())

for i in range(n):
    if i != 0:
        if pontos[i] == pontos[(i - 1)]:
            print('{}. {} ({})'.format(pos, times[i], pontos[i]))
        else:
            print('{}. {} ({})'.format((i + 1), times[i], pontos[i]))
            pos = i + 1
    else:
        print('{}. {} ({})'.format(pos, times[i], pontos[i]))

# Gustavoas 119210741
# UFCG 2019.2
