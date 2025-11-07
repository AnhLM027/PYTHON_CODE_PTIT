
n, m = map(int, input().split())

a = []
maxVal, minVal = 0, 1e6
for i in range(n):
    a.append(list(map(int, input().split())))
    maxVal = max(max(a[i]), maxVal)
    minVal = min(min(a[i]), minVal)

res = []
for i in range(n):
    for j in range(m):
        if a[i][j] == maxVal - minVal:
            res.append([i, j])
            
if res:
    print(maxVal - minVal)
    for index in res:
        print(f"Vi tri [{index[0]}][{index[1]}]")
else:
    print("NOT FOUND")