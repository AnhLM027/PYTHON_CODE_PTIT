
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

cnt = 0
cur = a[0]

for i in range(1, n):
    if a[i] > cur + k:
        cnt += 1
    cur = a[i]
print(cnt + 1)