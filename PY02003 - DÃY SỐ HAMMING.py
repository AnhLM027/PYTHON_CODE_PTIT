import bisect

LIMIT = 10**18
hamming = set()
for i in range(65):
    n2 = 1 << i
    if n2 > LIMIT: break
    for j in range(40):
        n3 = 3**j
        if n2 * n3 > LIMIT: break
        for k in range(28):
            n5 = 5 ** k
            val = n2 * n3 * n5
            if val > LIMIT: break
            hamming.add(val)

hamming = sorted(hamming)

for _ in range(int(input())):
    n = int(input())
    idx = bisect.bisect_left(hamming, n)
    print(idx + 1 if idx < len(hamming) and hamming[idx] == n else "Not in sequence")