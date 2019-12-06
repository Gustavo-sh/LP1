menor = 0
maior1 = 0
maior2 = 0
menor_valor = 0
maior_conforto = 0
maior_quarto = 0

while True:
    seq = input()
    if seq == '---':
        break
    seq2 = seq.split(',')
    if menor == 0 and menor_valor == 0:
        menor = float(seq2[0])
        menor_valor = seq2[3]
    if float(seq2[0]) < menor:
        menor = float(seq2[0])
        menor_valor = seq2[3]
    if float(seq2[1]) > maior2:
        maior2 = float(seq2[1])
        maior_quarto = seq2[3]
    if float(seq2[2]) > maior1:
        maior1 = float(seq2[2])
        maior_conforto = seq2[3]

while True:
    desejo = input()
    if desejo == 'fim':
        break
    if desejo == 'valor':
        print(menor_valor)
    elif desejo == 'tamanho':
        print(maior_quarto)
    elif desejo == 'conforto':
        print(maior_conforto)
