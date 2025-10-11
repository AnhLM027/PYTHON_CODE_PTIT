from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    a = [0] * int(1e6 + 5)
    for i in range(10, n + 1):
        if a[i] == 1:
            continue
        rev_i = int(''.join(reversed(str(i))))
        if rev_i > n: 
            continue
        
        if rev_i > i and is_prime(i) and is_prime(rev_i):
            a[rev_i] = 1
            print(i, rev_i, end=' ')
    print()

for tc in range(int(input().strip())):
    main()