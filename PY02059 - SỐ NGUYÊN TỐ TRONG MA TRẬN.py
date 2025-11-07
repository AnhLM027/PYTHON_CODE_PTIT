from math import sqrt

def snt(n: int):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res = []
maxSnt = 0
for i in range(n):
    for j in range(m):
        if snt(a[i][j]):
            maxSnt = max(a[i][j], maxSnt)

if maxSnt != 0:
    print(maxSnt)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxSnt:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")