
s = input()
k = int(input())
a = {}

for i in range(0, len(s), 2):
    t = s[i: i + 2]
    if len(t) == 2: a[t] = a.get(t, 0) + 1

a = dict(sorted(a.items(), key = lambda x: (int(x[0]), x[1])))

check = False
for x, y in a.items():
    if y >= k:
        print(x, y)
        check = True
if not check: print("NOT FOUND")