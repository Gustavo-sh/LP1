alvo = float(input())
soma = 0
media = 0
string = ''

while True:
    seq = input()
    if seq == 'fim':
        break
    seq2 = seq.split()
    for e in seq2:
        soma += float(e)
    media = soma / len(seq2)
    if media < (alvo / 2):
        break
    if media > alvo:
        for e in range(len(seq2) - 1):
            string += '{:.1f}'.format(float(seq2[e])) + ' '
        string += '{:.1f}'.format(float(seq2[len(seq2) - 1]))
    if string != '':
        print(string)
    soma = 0
    media = 0
    string = ''
