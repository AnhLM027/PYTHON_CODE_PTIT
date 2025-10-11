
def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
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
    

for _ in range(int(input())):
    main()