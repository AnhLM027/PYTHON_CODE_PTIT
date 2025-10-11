
def main():
    s1 = input().strip()
    s2 = ''.join(reversed(s1))
    check = True
    for i in range(1, len(s1), 1):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            check = False
    print("YES" if check else "NO")

for tc in range(0, int(input())):
    main()