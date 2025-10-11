from math import sqrt

def main():
    n = int(input())
    print("1", end='')
    i = 2
    while i <= int(sqrt(n)) + 1:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(f" * {i}^{cnt}", end='')
        i += 1
    if n > 1: print(f" * {n}^1", end='')
    print()

for tc in range(0, int(input())):
    main()