from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    a = list(range(n, 0, -1))

    res = []
    for v in permutations(a):
        res.append(''.join(map(str, v)))
        
    print(len(res))
    print(*res)