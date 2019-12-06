def cesar(msg, d):
    string = ''
    for e in msg:
        if d < 26:
            alvo = chr(ord(e) + d)
        elif d >= 27:
            alvo = chr(ord(e) + (d % 26))
        if e < 'a':
            string += e
        elif alvo < 'a':
            string += chr(ord(alvo) + 26)
        elif alvo > 'z':
            string += chr(ord(alvo) - 26)
        else:
            string += alvo
    return string
