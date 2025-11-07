import re

n, k = map(int, input().split())

freq = {}
for _ in range(n):
    s = input().lower()
    for w in re.split("[^a-z0-9]", s):
        if w == '': continue
        freq[w] = freq.get(w, 0) + 1

for w, f in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    if f >= k:
        print(w, f)