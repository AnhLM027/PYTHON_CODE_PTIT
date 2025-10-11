P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s = input()
    if s[0] == '0': break
    k, t = s.split()
    ans = [P[(P.index(x) + int(k)) % 28] for x in t]
    print(''.join(reversed(ans)))
    