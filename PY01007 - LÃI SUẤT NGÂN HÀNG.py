
def main():
    n, x, m = map(float, input().split())
    cnt = 0
    while n < m:
        n += x * n // 100
        cnt += 1
    print(cnt)

tc = int(input())
for _ in range(tc):
    main()