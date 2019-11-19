vezes = int(input())
somaa = 0
somar = 0
apro = 0
repro = 0

for e in range(vezes):
    notas = float(input())
    if notas < 7:
        somar += notas
        repro += 1
    elif notas >= 7:
        somaa += notas
        apro += 1

print('Reprovados: {}'.format(repro))
if repro != 0:
    print('Média: {:.1f}'.format(somar / repro))

print('')

print('Aprovados: {}'.format(apro))
if apro != 0:
    print('Média: {:.1f}'.format(somaa / apro))
