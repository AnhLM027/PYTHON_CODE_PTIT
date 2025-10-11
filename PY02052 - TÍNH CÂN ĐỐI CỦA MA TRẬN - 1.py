
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
k = int(input())

cheo1, cheo2 = 0, 0

for i in range(n):
    for j in range(n):
        if i > j: cheo1 += a[i][j]
        elif i < j: cheo2 += a[i][j]

tmp = abs(cheo1 - cheo2)      
print("YES" if tmp <= k else "NO")
print(tmp)

