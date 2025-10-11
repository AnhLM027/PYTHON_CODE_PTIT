
def main():
    global ans
    ans = 1e9
    n = input()
    minx = 0
    for i in range(len(n)):
        if n[i].isdigit():
            minx = minx * 10 + int(n[i])
        else:
            if minx != 0:
                ans = min(ans, minx)
            minx = 0
    print(ans)

tc = int(input())

while tc > 0:
    tc -= 1
    main()