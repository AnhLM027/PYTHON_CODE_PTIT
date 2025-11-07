
n = int(input())
a = []
for i in range(1, n + 1):
    a.append([input(), input(), input()])

for mh in sorted(a, key=lambda x: x[0]):
    print(*mh)
