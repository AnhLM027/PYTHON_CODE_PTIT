from collections import defaultdict, deque

n = int(input())
g = defaultdict(list)
indeg = defaultdict(int)
names = set()

for _ in range(n):
    a, op, b = input().split()
    names |= {a, b}
    if op == '>':
        g[a].append(b)
        indeg[b] += 1
    else:
        g[b].append(a)
        indeg[a] += 1

for x in names:
    indeg.setdefault(x, 0)

q = deque([x for x in names if indeg[x] == 0])
cnt = 0

while q:
    u = q.popleft()
    cnt += 1
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)

print("possible" if cnt == len(names) else "impossible")
