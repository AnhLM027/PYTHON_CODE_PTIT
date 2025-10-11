
s = input()
a = {}

for i in range(0, len(s), 2):
    t = s[i: i + 2]
    if len(t) == 2: a[t] = a.get(t, 0) + 1

for x, y in a.items(): print(x, y)