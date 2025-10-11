from math import sqrt

prime = [1] * int(1e4)
prime[0] = prime[1] = 0

for i in range(2, int(sqrt(1e4))):
    if prime[i]:
        for j in range(i * i, int(1e4), i):
            prime[j] = 0

a = [0]
for i in range(int(1e4)):
    if prime[i]: a.append(i)

n, x = map(int, input().split())

for i in range(n + 1):
    x += a[i]
    print(x, end=' ')
