
n = int(input())
a = list(map(int, input().split()))
while len(a) < n:
    a += list(map(int, input().split()))

maxVal = max(a)

res = []
for i in range(1, maxVal):
    if i not in a:
        res.append(i)
        
if not res: print("Excellent!")
else:
    for x in res: print(x)