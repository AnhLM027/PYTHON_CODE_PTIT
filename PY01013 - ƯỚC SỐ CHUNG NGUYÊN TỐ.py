import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    a, b = map(int, input().strip().split())
    c = math.gcd(a, b)
    
    sum = 0
    for d in str(c): sum += int(d)
    print("YES" if is_prime(sum) else "NO")

for tc in range(int(input().strip())):
    main()