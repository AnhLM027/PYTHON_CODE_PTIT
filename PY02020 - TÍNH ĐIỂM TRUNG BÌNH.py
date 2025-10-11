
n, a = int(input()), list(map(float, input().split()))
a.sort()

maxn, minn = max(a), min(a)
sum = sum(a)
c1, c2 = 0, 0
for x in a:
    if x == maxn: c1 += 1
    if x == minn: c2 += 1
print(f"{(sum - maxn * c1 - minn * c2) / (n - c1 - c2):.2f}")
