import sys, re, heapq

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = ' ' + sys.stdin.readline().replace(' ', '  ') + ' '
    a = []
    for i in range(-8, 9):
        if len(a) >= 4:
            break
        if i == 0:
            continue
        pattern = ('-' if i < 0 else ' ') + r'\d' * abs(i) + ' '
        a += [int(x) for x in re.findall(pattern, line)]
    print(sum(heapq.nsmallest(3, a)))