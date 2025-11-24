from itertools import combinations

n, k = map(int, input().split())
a = set(input().split())

a = list(sorted(a))

for c in combinations(a, k): print(*c)
