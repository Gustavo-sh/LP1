palavra = input()
quant = input()
string = ''
bug = list(palavra)
for e in range(len(palavra)):
    string += palavra[e]
    for i in range(len(bug) - 1, -1, -1):
        for v in range(int(quant[i])):
            string += palavra[e]
        bug.pop()
        break

print(string)

# aleluia
