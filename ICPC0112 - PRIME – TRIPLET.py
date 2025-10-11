from math import sqrt

prime, a = [1 for i in range(int(1e6 + 5))], []
prime[0] = prime[1] = 0

for i in range(2, int(sqrt(1e6 + 5)) + 1):
    if prime[i]:
        for j in range(i * i, int(1e6 + 5), i):
            prime[j] = 0
            
for i in range(2, int(1e6 + 5)):
    if prime[i]:
        a.append(i)

prefix_sum = [0 for i in range(int(1e6) + 5)]

cnt = 0
for i in range(len(a) - 2):
    if a[i + 2] - a[i] == 6 and (a[i + 2] - a[i + 1] == 4 or a[i + 2] - a[i + 1] == 2):
        cnt += 1
        prefix_sum[a[i + 2]] = cnt

for i in range(1, int(1e6) + 5):
    if prefix_sum[i] == 0:
        prefix_sum[i] = prefix_sum[i - 1]

def main():
    n = int(input())
    print(prefix_sum[n])

tc = int(input())
while tc > 0:
    tc -= 1
    main()