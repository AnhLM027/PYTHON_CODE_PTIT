import re

freq = {}
for _ in range(int(input())):
    s = input().lower()
    for w in re.split("[^a-z0-9]", s):
        if w == '': continue
        freq[w] = freq.get(w, 0) + 1

for w, f in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    print(w, f)