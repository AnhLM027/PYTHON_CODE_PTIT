
while True:
    a, b, c, d = list(map(int, input().split()))
    if a == b == c == d == 0: break
    cnt = 0
    while True:
        if a == b and a == c and a == d: break
        tmp = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - tmp)
        cnt += 1
    print(cnt)