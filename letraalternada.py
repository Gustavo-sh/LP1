palavra = input()
string = ''

for e in range(0, len(palavra), 2):
    string += str(palavra[e])

print(string)
