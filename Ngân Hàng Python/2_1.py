
for _ in range(int(input())):
    s, k = input().split()
    k = int(k) % 26
    
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            tmp = ord('a')
        else:
            tmp = ord('A')
            
        res += chr((ord(c) - tmp + k) % 26 + tmp)
    print(res)