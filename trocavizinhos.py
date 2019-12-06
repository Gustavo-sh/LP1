def troca_vizinhos_condicional(seq):
    if len(seq) % 2 == 1:
        for e in range(0, len(seq) - 1, 2):
            if seq[e][0] > seq[e + 1][0]:
                seq[e], seq[e + 1] = seq[e + 1], seq[e]
    else:
        for e in range(0, len(seq), 2):
            if seq[e][0] > seq[e + 1][0]:
                seq[e], seq[e + 1] = seq[e + 1], seq[e]
    print(seq)
    return seq
