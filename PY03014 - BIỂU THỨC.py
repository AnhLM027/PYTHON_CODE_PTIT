
t = int(input())
for _ in range(t):
    s = input()
    cnt = 1
    a = []
    for c in s:
        if c == '(':
            a.append(cnt)
            print(cnt, end=' ')
            cnt += 1
        elif c == ')':
            print(a.pop(), end=' ')
    print()
