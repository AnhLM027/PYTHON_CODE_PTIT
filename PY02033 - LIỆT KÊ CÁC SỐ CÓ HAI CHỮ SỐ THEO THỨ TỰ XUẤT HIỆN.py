
s = input()
a = []

for i in range(0, len(s), 2):
    t = s[i: i + 2]
    if len(t) == 2 and t not in a: a.append(t) 

for x in a: print(x, end=' ')