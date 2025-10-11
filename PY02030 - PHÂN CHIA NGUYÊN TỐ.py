from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))

b = []
r = 0
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
        r += a[i]

l = 0
check = False
for i in range(len(b) - 1):
    l += b[i]
    r -= b[i]
    if snt(l) and snt(r):
        check = True
        print(i)
        break
if not check: print("NOT FOUND")