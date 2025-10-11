

def gt(n):
    if n == 0 or n == 1: return 1
    else: return n * gt(n - 1)

def main():
    s = input()
    tmp = 0
    for c in s:
        tmp += gt(int(c))
    print("Yes" if tmp == int(s) else "No")


for tc in range(int(input())):
    main()