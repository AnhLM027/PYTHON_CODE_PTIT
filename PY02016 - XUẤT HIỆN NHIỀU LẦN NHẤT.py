from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    x, y = max(cnt.items(), key=lambda x : x[1])
    if y > n // 2: print(x)
    else: print("NO")

for tc in range(int(input())):
    main()