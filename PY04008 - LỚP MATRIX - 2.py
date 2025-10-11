
t = int(input())
inp = []
while True:
    try: inp.extend(map(int, input().split()))
    except: break

cnt = 0

def main():
    global cnt
    n, m = inp[cnt], inp[cnt + 1]
    cnt += 2
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = inp[cnt + j]
        cnt += m
    
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(n):
                res[i][k] += a[i][j] * b[j][k]

    for i in range(n):
        for j in range(n): print(res[i][j], end=' ')
        print()
    

for _ in range(t):
    main()