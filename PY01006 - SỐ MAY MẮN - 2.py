
def main():
    check = True
    for c in input():
        if c != '4' and c != '7':
            check = False
            break
    print("YES" if check else "NO")

tc = int(input())
for _ in range(tc):
    main()