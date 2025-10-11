
def main():
    a, k, n = map(int, input().strip().split())
    check = False
    b = k - a % k
    check = False
    while a + b <= n:
        check = True
        print(b, end=' ')
        b += k
    if not check: print(-1)

# for tc in range(int(input().strip())):
main()