
for _ in range(int(input())):
    n = int(input())
    se = set()
    maxn, minn = -1e9, 1e9
    a = list(map(int, input().split()))
    for x in a:
        se.add(x)
        maxn = max(maxn, x)
        minn = min(minn, x)
    print(maxn - minn + 1 - len(se))
