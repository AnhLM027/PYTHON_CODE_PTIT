
for _ in range(int(input())):
    line = input().strip()
    ws = line.split()
    noti, l = [], 0
    for w in ws:
        if l == 0:
            if len(w) <= 100:
                noti.append(w)
                l += len(w)
        else:
            if l + 1 + len(w) <= 100:
                noti.append(w)
                l += 1 + len(w)
            else: break
    print(' '.join(noti))