
n = int(input())
res = []
S = 0
for i in range(n):
    a = list(map(int,  input().split()))
    res.append(a)
    S += sum(a)
    
if n == 2: print(1, S // 2 - 1)
else:
    tmp = (sum(res[0]) - S // ((n - 1) * 2)) // (n - 2)
    print(tmp, end=' ')
    for i in range(1, n):
        print(res[0][i] - tmp, end=' ')
    