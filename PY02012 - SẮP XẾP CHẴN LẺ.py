n = int(input())
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
    
chan = []
le = []
for i in a:
    if i % 2 == 0: chan.append(i)
    else: le.append(i)

chan.sort()
le.sort(key= lambda x: -x)

cnt1, cnt2 = 0, 0
for i in range(0, n):
    if a[i] % 2 == 0:
        print(chan[cnt1], end=' ')
        cnt1 += 1
    else:
        print(le[cnt2], end=' ')
        cnt2 += 1