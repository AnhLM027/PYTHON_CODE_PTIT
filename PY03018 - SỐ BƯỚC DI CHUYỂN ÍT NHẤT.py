from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = [[-1] * m for _ in range(n)]
    ans[0][0] = 0
    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()

        if i + 1 < n:
            d = abs(a[i + 1][j] - a[i][j])
            if d and i + d < n and ans[i + d][j] == -1:
                ans[i + d][j] = ans[i][j] + 1
                q.append((i + d, j))

        if j + 1 < m:
            r = abs(a[i][j + 1] - a[i][j])
            if r and j + r < m and ans[i][j + r] == -1:
                ans[i][j + r] = ans[i][j] + 1
                q.append((i, j + r))

        if i + 1 < n and j + 1 < m:
            dr = abs(a[i + 1][j + 1] - a[i][j])
            if dr and i + dr < n and j + dr < m and ans[i + dr][j + dr] == -1:
                ans[i + dr][j + dr] = ans[i][j] + 1
                q.append((i + dr, j + dr))

    print(ans[-1][-1])
