from sys import stdin
from array import array

data = stdin.buffer.read().split()
n = int(data[0])
nums = list(map(int, data[1:]))

maxN = max(nums)

spf = array('i', [0]) * (maxN + 1)
sumPF = array('i', [0]) * (maxN + 1)
primes = []

# ---- SIEVE (linear) ----
for i in range(2, maxN + 1):
    if not spf[i]:
        spf[i] = i
        primes.append(i)

    si = spf[i]
    for p in primes:
        if p > si or p * i > maxN:
            break
        spf[p * i] = p

# ---- TÍNH SUM PF ----
for i in range(2, maxN + 1):
    sp = spf[i]
    sumPF[i] = sp + sumPF[i // sp]

# ---- OUTPUT ----
total = 0
for x in nums:
    total += sumPF[x]

print(total)
