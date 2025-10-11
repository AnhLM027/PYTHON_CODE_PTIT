
def main():
    s = input().strip()
    print("YES" if s[0:2] == s[-2:] else "NO")

for tc in range(int(input().strip())):
    main()