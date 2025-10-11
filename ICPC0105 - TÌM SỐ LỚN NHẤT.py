
def main():
    global ans
    ans = -1e9
    n = input()
    maxn = 0
    for i in range(len(n)):
        if n[i].isdigit():
            maxn = maxn * 10 + int(n[i])
        else:
            ans = max(ans, maxn)
            maxn = 0
    print(max(ans, maxn))

tc = int(input())

while tc > 0:
    tc -= 1
    main()