
for _ in range(int(input())):
    n, p = map(int, input().split())
    cnt, pk = 0, p
    while pk <= n:
        cnt += n // pk
        pk *= p
    print(cnt)
    