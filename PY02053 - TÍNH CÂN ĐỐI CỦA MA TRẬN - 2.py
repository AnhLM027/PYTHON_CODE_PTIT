
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
k = int(input())

cheo1, cheo2 = 0, 0

for i in range(n):
    for j in range(n):
        if i + j < n - 1: cheo1 += a[i][j]
        elif i + j >= n: cheo2 += a[i][j]

tmp = abs(cheo1 - cheo2)      
print("YES" if tmp <= k else "NO")
print(tmp)

