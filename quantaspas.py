razao = int(input())
teste = 1
printar = 0

while True:
    seq = input()
    if seq == 'fim':
        break
    seq2 = seq.split()
    for e in range(1, len(seq2)):
        if int(seq2[e]) == (int(seq2[e - 1]) + razao):
            teste += 1
    if teste  == len(seq2):
        printar += 1
    teste = 1

print(printar)
