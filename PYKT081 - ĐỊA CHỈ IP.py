
t = int(input())
for _ in range(t):
    IP = input().split('.')
    
    
    check = True
    for x in IP:
        try:
            if int(x) < 0 or int(x) > 255: check = False
        except: check = False
    
    print("YES" if check and len(IP) == 4 else "NO") 