

def main():
    n = input()
    check = True
    for i in range(1, len(n)):
        if n[i] == n[i - 1] or (i > 1 and n[i] != n[i - 2]):
            check = False
            break
    print("YES" if check else "NO")

for tc in range(int(input())):
    main()