
def main():
    a = {2: 1, 4: 2, 8: 3, 16: 4}
    hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    k = int(f.readline())
    s = f.readline().strip()
    n = a[k]
    while len(s) % n != 0:
        s = "0" + s
    ans = ""

    for i in range(0, len(s), n):
        tmp = 0
        for j in s[i:i+n]:
            tmp = tmp * 2 + int(j)
        if(k == 16):
            tmp = hex[tmp] if tmp in hex else str(tmp)
        ans += str(tmp)
        
    print(ans)

f = open('DATA.in', 'r')

tc = int(f.readline())
while tc > 0:
    tc -= 1
    main()