
s1, s2 = input().lower().split(), input().lower().split()
se1, se2 = set(), set()

for t in s1:
    se1.add(t)
    for v in s2:
        se1.add(v)
        if t == v: se2.add(t)

print(' '.join(sorted(se1)))
print(' '.join(sorted(se2)))