from math import gcd

def main():
    n = int(input())
    sum = 0
    if n & 1:
        for i in range(1, n + 1, 2):
            sum += float(1 / i)
    else:
        for i in range(2, n + 1, 2):
            sum += float(1 / i)
    print(f"{sum:.6f}")

for tc in range(int(input())):
    main()