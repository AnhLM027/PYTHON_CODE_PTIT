import re

res = []

for _ in range(int(input())):
    s = input()
    r = re.split(r"[a-zA-Z]+", s)
    for w in r:
        if w == '': continue
        res.append(int(w))
    
res.sort()
for x in res:
    print(x)