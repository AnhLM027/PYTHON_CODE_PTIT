from math import sqrt

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = input()
    sum = 0
    for d in n:
        if not is_prime(int(d)):
            print("No")
            return
        sum += int(d)
    if is_prime(int(n)) and is_prime(sum) and is_prime(int(''.join(reversed(n)))):
        print("Yes")
    else:
        print("No")

for tc in range(int(input())):
    main()