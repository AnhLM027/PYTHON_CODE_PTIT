import sys
from math import *

data = sys.stdin.read().split()

n = int(data[0])
i = 1

for _ in range(n):
    p = list(map(int, data[i:i + 6]))
    i += 6
    a = p[:2]
    b = p[2 : 4]
    c = p[4:]
    AB = sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    BC = sqrt(pow(c[0] - b[0], 2) + pow(c[1] - b[1], 2))
    AC = sqrt(pow(a[0] - c[0], 2) + pow(a[1] - c[1], 2))
    
    if AB + BC > AC and AB + AC > BC and BC + AC > AB:
        print(f"{AB + BC + AC:.6f}")
    else: print("INVALID")