from collections import deque

n = int(input())

digits = ['2', '3', '5', '7']
q = deque(digits)
res = []

while q:
    s = q.popleft()
    if len(s) > n:
        continue
    if len(s) >= 4 and all(d in s for d in digits) and s[-1] != '2':
        res.append(int(s))
    for d in digits:
        q.append(s + d)

res.sort()
for x in res:
    print(x)