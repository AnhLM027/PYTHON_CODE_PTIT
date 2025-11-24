
a, n = [], int(input())
for _ in range(n): a.append(input())

def turn(des, src):
    if des == src: return 0
    for i in range(1, len(des)+1):
        src = src[1:] + src[0]
        if src == des: return i
    return -1

ans = 10**5
for i in range(n):
    cnt = 0
    for j in range(n):
        num = turn(a[i], a[j])
        if num == -1:
            cnt = -1
            break
        cnt += num
    if cnt != -1:
        ans = min(ans, cnt)

print(ans if ans != 10**5 else -1)