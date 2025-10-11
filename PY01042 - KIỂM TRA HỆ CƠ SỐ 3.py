

def main():
    n = input()
    i = 0
    while i < len(n) and '0' <= n[i] <= '2': i += 1
    print("YES" if i == len(n) else "NO")

for tc in range(int(input())):
    main()