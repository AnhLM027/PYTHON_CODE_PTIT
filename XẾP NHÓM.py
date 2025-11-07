from bisect import bisect_right
from itertools import accumulate

def max_groups(a, k):
    a.sort()
    prefix = [0] + list(accumulate(a))
    n = len(a)
    l, r = 0, sum(a) // k
    while l < r:
        m = (l + r + 1) // 2
        idx = bisect_right(a, m)
        total = prefix[idx] + (n - idx) * m
        if total >= k * m: l = m
        else: r = m - 1
    return l

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_groups(a, k))
