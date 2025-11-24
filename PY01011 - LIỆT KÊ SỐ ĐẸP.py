
res = []

def Try(i, n, s):
    if len(s) and s[0] == '0': return
    
    if i == n:
        res.append(int(s + s[::-1]))
        return
    
    for d in "02468":
        Try(i + 1, n, s + d)
        
for l in range(1, 4): Try(0, l, "")

res.sort()

for _ in range(int(input())):
    n = int(input())
    for x in res:
        if x < n: print(x, end=' ')
        else: break
    print()