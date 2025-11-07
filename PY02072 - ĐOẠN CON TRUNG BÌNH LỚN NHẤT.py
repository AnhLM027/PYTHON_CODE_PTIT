
n = int(input())
a = list(map(int, input().split()))

mean = max(a)
cnt, maxCnt = 0, 0
for i in range(n):
    if a[i] == mean: cnt += 1
    else: cnt = 0
    maxCnt = max(maxCnt, cnt)

print(maxCnt)