from math import gcd

n, k = map(int, input().split())
cnt = 0

for i in range(pow(10, k - 1), pow(10, k) - 1, 1):
    if gcd(n, i) == 1:
        print(i, end=' ')
        cnt += 1
        if cnt % 10 == 0:
            print()
            