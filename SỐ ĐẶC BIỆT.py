


def main():
    n, k = map(int, input().split())
    ans = 0
    MOD = int(1e9 + 7)
    cnt = 0
    while(k > 0):
        if k % 2 == 1: ans += pow(n, cnt)
        cnt += 1
        k //= 2
    print(ans % MOD)

for tc in range(int(input())):
    main()