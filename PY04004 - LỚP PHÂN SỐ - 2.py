from math import gcd

a, b, c, d = map(int, input().split())
tu = a * d + c * b
mau = b * d
print(f'{tu//gcd(tu, mau)}/{mau//gcd(tu, mau)}')