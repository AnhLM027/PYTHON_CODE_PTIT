from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n, m = map(int, input().split())
for i in range(n):
    print(*(1 if snt(x) else 0 for x in map(int, input().split())))

