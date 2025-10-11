
def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    b = []
    for _ in range(3):
        b.append(list(map(int, input().split())))
    
    sum = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for k in range(3):
                for l in range(3):
                    sum += a[i + k][j + l] * b[k][l]
    
    print(sum)

for tc in range(int(input().strip())):
    main()