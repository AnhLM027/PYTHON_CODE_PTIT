from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def cnt(n):
    if n <= 1: return 0
    if snt(n): return 0
    d = 1
    while True:
        if snt(n - d): return d
        if snt(n + d): return d
        d += 1

n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))
    
ans = 0
for x in a:
    ans = max(ans, cnt(x))

print(ans)