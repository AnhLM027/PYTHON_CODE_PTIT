
def main():
    s = input()
    cur = s[0]
    for c in s:
        if c.isdigit():
            for i in range(0, int(c), 1):
                print(cur, end='')
        else: cur = c
    print()

for tc in range(int(input().strip())):
    main()