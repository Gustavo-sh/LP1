def meu_join(delimitador, sequencia_de_string):
    string = ''
    for e in range(len(sequencia_de_string)):
        if e == len(sequencia_de_string) - 1:
            string += sequencia_de_string[e]
            return string
        string += sequencia_de_string[e] + delimitador
