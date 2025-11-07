
for _ in range(int(input())):
    n = int(input())
    while n % 2 == 0: n //= 2
    
    cnt, p = 1, 3
    while p * p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        cnt *= k + 1
        p += 2
        
    if n > 1: cnt *= 2
    print(cnt - 1)
