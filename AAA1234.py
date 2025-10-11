import itertools
s = input().strip()

for hv in itertools.permutations(s):
    print(''.join(hv))
