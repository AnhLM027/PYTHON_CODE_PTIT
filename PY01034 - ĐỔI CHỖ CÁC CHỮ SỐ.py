
for _ in range(int(input())):
    n = list(input().strip())
    check = False
    index = 0
    for i in range(len(n) - 1, 0, -1):
        if n[i] < n[i - 1]:
            index = i - 1
            maxVal = '0'
            for c in n[i:]:
                if c < n[i - 1] and c > maxVal: maxVal = c
            
            j = i
            while j < len(n) and n[j] != maxVal: j += 1
            
            n[index], n[j] = n[j], n[index]
            
            check = True
            break
        
    if n[0] == '0' or check == False: print(-1)
    else: print(''.join(n))
