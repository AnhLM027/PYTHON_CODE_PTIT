
for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    check = True
    for i in range(n): 
        if a[i] > b[i]:
            check = False
    print("YES" if check else "NO")
