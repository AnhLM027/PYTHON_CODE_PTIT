import re

n = int(input())

freq = {}
for _ in range(n):
    s = input().lower()
    for w in re.split("[^a-z]", s):
        if w == '': continue
        freq[w] = freq.get(w, 0) + 1

for w, f in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    print(w, f)