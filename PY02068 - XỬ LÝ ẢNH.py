
t = int(input())
for _ in range(t):
    n, m, L = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ps = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ps[i][j] = a[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]

    res = []
    for i in range(L, n + 1):
        row = []
        for j in range(L, m + 1):
            total = ps[i][j] - ps[i - L][j] - ps[i][j - L] + ps[i - L][j - L]
            row.append(total // (L * L))
        res.append(row)

    for r in res:
        print(*r)
