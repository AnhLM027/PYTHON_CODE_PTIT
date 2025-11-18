from itertools import combinations

n, k = map(int, input().split())
a = set(list(map(int, input().split())))
    
for v in combinations(sorted(a, key=lambda x: x), k):
    print(*v)