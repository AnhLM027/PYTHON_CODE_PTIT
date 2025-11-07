
n = int(input())
lines = [input().strip() for _ in range(n)]

res = []
i = 0
while i < n:
    if lines[i] == '':
        i += 1
        continue
    topic = lines[i]
    cnt = 0
    i += 1
    while i < n and lines[i] != '':
        cnt += 1
        i += 1
    res.append((topic, cnt))

for t, c in res:
    print(f"{t}: {c}")
