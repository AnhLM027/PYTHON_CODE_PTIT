

def main():
    n = input()
    i = 0
    while i < len(n) - 1 and n[i] < n[i + 1]: i += 1
    while i < len(n) - 1 and n[i] > n[i + 1]: i += 1
    print("YES" if i == len(n) - 1 and len(n) >= 3 else "NO")

for tc in range(int(input())):
    main()