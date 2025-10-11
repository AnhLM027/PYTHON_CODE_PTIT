
def main():
    s, t = input(), input()
    n, cnt = len(t), 0
    i = 0
    while i <= len(s) - n + 1:
        if s[i:i+n] == t:
            cnt += 1
            i += n
        else: i += 1
    print(cnt)


for tc in range(int(input())):
    main()