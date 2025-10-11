
s = input()
a = set()

for i in range(0, len(s), 2):
    if len(s[i: i + 2]) == 2: a.add(s[i: i + 2]) 

a = sorted(a, key = lambda x: int(x))
for x in a: print(x, end=' ')