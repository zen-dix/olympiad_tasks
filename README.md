s = "abcabcbb"
max_lenght = 0
sub = ""
for symb in s:
  if symb not in sub:
    sub.append(symb)
  else:
    sub.pop(0)
print(sub)
