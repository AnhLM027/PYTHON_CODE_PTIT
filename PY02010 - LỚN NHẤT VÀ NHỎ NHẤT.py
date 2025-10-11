
while True:
    n = int(input())
    if n == 0: break

    a = set()
    for _ in range(n): a.add(int(input()))
    a = sorted(a)
    if(a[0] == a[-1]): print("BANG NHAU")
    else: print(a[0], a[-1])