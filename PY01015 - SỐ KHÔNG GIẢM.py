
def main():
    s = input()
    check = False
    for i in range(0, len(s) - 1, 1):
        if s[i] > s[i + 1]:
            check = True
            break
    print("YES" if not check else "NO")

for tc in range(int(input().strip())):
    main()