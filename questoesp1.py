quant = 0
total = 0
somar = 0
lista = []

while True:
    if quant == 0:
        name = input()
        if name == '**': break
        lista.append(name)
        quant += 1
    if quant == 1:
        questoes = input()
        if questoes == '*':
            quant = 0
            lista.append(somar)
            somar = 0
            continue
        if questoes == '**':
            lista.append(somar)
            break
        somar += int(questoes)
        total += int(questoes)

print('Relatório de novas questões:')
print('')

for e in range(0, len(lista), 2):
    print('{}: {}'.format(lista[e], lista[e + 1]))
print('---')
print('Total de novas questões: {}'.format(total))
