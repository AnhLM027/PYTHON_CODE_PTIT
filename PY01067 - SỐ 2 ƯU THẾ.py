from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    q = deque(['0', '1', '2'])
    res = []
    while len(res) < n:
        s = q.popleft()
        if s[0] != '0':
            if s.count('2') > len(s) / 2:
                res.append(s)
        for c in '012':
            q.append(s + c)
    print(*res)
