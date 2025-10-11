

def cnt(n: int):
    res = [0] * 10
    num = 1
    while n >= num:
        low = n % num
        cur = (n // num) % 10
        high = n // (num * 10)
        for i in range(0, 10):
            res[i] += high * num
        for i in range(0, cur):
            res[i] += num
        res[cur] += low + 1
        if num >= 1: res[0] -= num
        num *= 10
    return res

def main():
    l, r = map(int, input().split())
    x = cnt(l - 1)
    y = cnt(r)
    for i in range(0, 10):
        print(y[i] - x[i], end=' ')
    print()

for tc in range(int(input())):
    main()