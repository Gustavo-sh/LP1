def senha_segura(senha):
    if len(senha) < 4:
        return 'Senha insegura'
    for e in range(len(senha)):
        if e % 2 == 0:
            if int(senha[e]) % 2 == 0:
                return 'Senha insegura'
        if e % 2 == 1:
            if int(senha[e]) % 2 == 1:
                return 'Senha insegura'
    return 'Senha segura'
