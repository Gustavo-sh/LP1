def char_unico(string):
  stringg = ''
  for e in range(len(string) - 1):
    if e == 0:
      if string[e + 1] != string[e]:
        return string[e]
    elif string[-1] != string[-2]:
      return string[-1]
    else:
      if string[e - 1] != string[e] and string[e + 1] != string[e]:
        return string[e]
  return stringg
