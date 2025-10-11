from math import log2

MOD = int(1e9 + 7)

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 0
    while k > 0:
        p = int(log2(k))
        ans += pow(n, p)
        k -= pow(2, p)
    print(ans % MOD)
