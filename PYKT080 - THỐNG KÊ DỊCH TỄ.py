

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
vis = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

def dfs(x, y):
    global ans
    for k in dir:
        x1 = x + k[0]
        y1 = y + k[1]
        if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m or vis[x1][y1] == True: continue
        else:
            ans += a[x1][y1]
            vis[x1][y1] = True

for i in range(n):
    for j in range(m):
        if(a[i][j] == -1):
            dfs(i, j)

print(ans)