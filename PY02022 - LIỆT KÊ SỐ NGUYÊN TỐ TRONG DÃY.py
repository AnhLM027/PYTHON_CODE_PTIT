from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n, a = int(input()), list(map(int, input().split()))

mp = {}
for x in a:
    if snt(x): mp[x] = mp.get(x, 0) + 1
    
for x, y in mp.items():
    print(x, y)