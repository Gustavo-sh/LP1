alvo = int(input())
mults = 0

while True:
    seq = input()
    if seq == 'fim': break
    seq2 = seq.split()
    mu1 = str(int(seq2[0]) / alvo)
    mu2 = str(int(seq2[1]) / alvo)
    if mu1[2] == '0' and mu2[2] == '0':
        mults += 1

print(mults)
