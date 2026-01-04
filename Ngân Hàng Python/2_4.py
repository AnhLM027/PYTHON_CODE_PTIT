
for _ in range(int(input())):
    s = input()
    mp = {}
    
    max_cnt = 0
    res = s[0]
    
    for c in s:
        mp[c] = mp.get(c, 0) + 1
        if mp.get(c, 0) > max_cnt:
            max_cnt = mp.get(c, 0)
            res4 = c
    print(c)