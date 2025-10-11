from math import gcd

a, b = map(int, input().split())
k = gcd(a, b)
print(f'{a//k}/{b//k}')