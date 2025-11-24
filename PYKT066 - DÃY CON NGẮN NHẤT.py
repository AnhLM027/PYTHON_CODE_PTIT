from math import gcd
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = []
    while len(a) < n:
        try:
            a.extend(map(int, input().split()))
        except:
            break

    res = float('inf')
    for i in range(n):
        g = 0
        for j in range(i, n):
            g = gcd(g, a[j])
            if g < k: break
            if g == k:
                res = min(res, j - i + 1)
                break
    print(res if res != float('inf') else -1)