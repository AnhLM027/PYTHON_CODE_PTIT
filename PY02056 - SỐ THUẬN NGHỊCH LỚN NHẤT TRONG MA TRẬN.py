from math import sqrt

def tn(n: int):
    if n < 10: return False
    s = str(n)
    l = 0; r = len(s) - 1
    while(l < r):
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res = []
maxVal = 0
for i in range(n):
    for j in range(m):
        if tn(a[i][j]):
            maxVal = max(a[i][j], maxVal)

if maxVal != 0:
    print(maxVal)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxVal:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")