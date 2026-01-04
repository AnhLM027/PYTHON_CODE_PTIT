
for _ in range(int(input())):
    s = input()
    mp = {}
    
    for c in s:
        mp[c] = mp.get(c, 0) + 1
        
    r1 = ""
    r2 = ""
    for x, y in mp.items():
        if y == 1: r1 += x
        else: r2 += x
    print(r1 if r1 else "NONE")
    print(r2 if r2 else "NONE")