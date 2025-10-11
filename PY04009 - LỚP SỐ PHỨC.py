

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    t1, a1 = a + c, b + d
    c1 = a * t1 - b * a1
    c2 = t1 * b + a1 * a
    d1 = t1 * t1 - a1 * a1
    d2 = 2 * t1 * a1
    print(c1, end = ' ')
    if c2 > 0: print("+", c2, end='i')
    else: print("-", abs(c2), end='i')
    print(",", d1, end=' ')
    if d2 > 0: print("+", d2, end='i')
    else: print("-", abs(d2), end='i')
    print()
