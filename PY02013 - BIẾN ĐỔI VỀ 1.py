
while True:
    n = int(input())
    if n == 0: break
    a = set()
    while n != 1:
        if n & 1: n = n * 3 + 1
        else: n = int(n / 2)
        a.add(n)
    print(len(a) + 1)