import math
from math import gcd

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            cnt += 1
    print("YES" if is_prime(cnt) else "NO")

tc = int(input())
for _ in range(tc):
    main()