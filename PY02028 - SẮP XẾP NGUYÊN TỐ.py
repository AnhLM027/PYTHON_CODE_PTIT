from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))

ind, num = [], []
for i in range(n):
    if snt(a[i]):
        ind.append(i)
        num.append(a[i])

num = sorted(num, key = lambda x: x)

i = 0
while i < len(ind):
    a[ind[i]] = num[i]
    i += 1

for x in a: print(x, end=' ')