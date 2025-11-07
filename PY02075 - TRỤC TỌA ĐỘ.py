

for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    a = sorted(a, key=lambda x: (x[1], x[0]))
    cnt = 1
    st = a[0][0]; en = a[0][1]
    
    for i in range(1, n):
        if a[i][0] >= en:
            st = a[i][0]
            en = a[i][1]
            cnt += 1
            
    print(cnt)