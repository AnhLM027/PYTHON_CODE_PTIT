from math import *

p1 = map(float, input().split())
p2 = map(float, input().split())

lo1, l1 = p1
lo2, l2 = p2

dl = l2 - l1
dlo = lo2 - lo1

a = pow(sin(dl / 2), 2) + cos(l1) * cos(l2) * pow(sin(dlo / 2), 2)
c = 2 * asin(sqrt(a))
print(f"{6371 * c:.2f}")