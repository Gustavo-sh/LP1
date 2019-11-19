alvo = int(input())
soma = 0
media = 0
string = ''

while True:
    seq = input()
    if seq == '-':
        break
    seq2 = seq.split()
    for e in seq2:
        soma += int(e)
    if soma >= alvo:
        for e in range(len(seq2) - 1):
            string += (seq2[e] + ' ' + '+' + ' ')
        string += (seq2[len(seq2) - 1] + ' ' + '=' + ' ' + str(soma))
        print(string)
    if soma > (5 * alvo): break
    soma = 0
    media = 0
    string = ''
