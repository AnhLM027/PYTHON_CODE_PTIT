from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def kc(self, p):
        return sqrt(pow(self.x - p.x, 2) + pow(self.y - p.y, 2))

cnt = 0

def main(l):
    global cnt
    a, b, c, d, e, f = l[cnt: cnt + 6]
    cnt += 6
    
    p1 = Point(a, b)
    p2 = Point(c, d)
    p3 = Point(e, f)
    x = p1.kc(p2)
    y = p2.kc(p3)
    z = p3.kc(p1)
    if x + y > z and y + z > x and z + x > y: print(f'{x + y + z:.3f}')
    else: print("INVALID")

t = int(input())
l = []
for i in range(t): l.extend([float(x) for x in input().split()])
for j in range(t):
    main(l)