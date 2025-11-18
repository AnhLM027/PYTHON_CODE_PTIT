
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

if n > m:
    rm = []
    for i in range(n):
        if i % 2 == 0: rm.append(i)
        if n - len(rm) == m: break
    a = [a[i] for i in range(n) if i not in rm]
elif m > n:
    rm = []
    for j in range(m):
        if j % 2 == 1: rm.append(j)
        if m - len(rm) == n: break
    a = [[a[i][j] for j in range(m) if j not in rm] for i in range(n)]

for row in a:
    print(*row)
