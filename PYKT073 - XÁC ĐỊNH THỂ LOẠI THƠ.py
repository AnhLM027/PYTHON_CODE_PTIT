
n = int(input())
lines = [input().strip() for _ in range(n)]
res = []

i = 0
while i < n:
    if i + 3 < n and all(len(lines[i + j].split()) == 7 for j in range(4)):
        res.append(2)
        i += 4
    elif i + 1 < n and len(lines[i].split()) == 6 and len(lines[i + 1].split()) == 8:
        while i + 1 < n and len(lines[i].split()) == 6 and len(lines[i + 1].split()) == 8:
            i += 2
        res.append(1)
    else: i += 1
    
print(len(res))
for x in res: print(x)