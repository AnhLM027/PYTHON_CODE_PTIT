
for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    
    mp = {}
    for x in a:
        mp[x] = mp.get(x, 0) + 1

    ans = 0
    for x, y in mp.items():
        if y & 1: ans = x
    print(ans)