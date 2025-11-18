from itertools import permutations

s = input().strip()

for v in permutations(s):
    print(''.join(v))