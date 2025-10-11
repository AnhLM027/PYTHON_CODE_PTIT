
def main():
    n, cnt = int(input()), 0
    a = sorted([int(x) for x in input().split()])
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == 0:
                cnt += 1
                l += 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    print(cnt)

tc = int(input())
while tc > 0:
    tc -= 1
    main()