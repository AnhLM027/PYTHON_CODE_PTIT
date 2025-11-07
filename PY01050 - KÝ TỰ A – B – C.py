from collections import deque

n = int(input())
q = deque(['A', 'B', 'C'])
r = []

while q:
    s = q.popleft()
    if len(s) <= n:
        a, b, c = s.count('A'), s.count('B'), s.count('C')
        if all(x in s for x in 'ABC') and a <= b <= c: r.append(s)
        if len(s) < n:
            for ch in 'ABC': q.append(s + ch)

r.sort(key=lambda x: (len(x), x))
print("\n".join(r))