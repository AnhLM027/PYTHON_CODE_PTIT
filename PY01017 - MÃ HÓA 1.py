
def main():
    s = input()
    cur = s[0]
    cnt = 0
    for c in s:
        if c == cur:
            cnt += 1
        else:
            print(str(cnt) + cur, end='')
            cur = c
            cnt = 1
    print(str(cnt) + cur)

for tc in range(int(input().strip())):
    main()