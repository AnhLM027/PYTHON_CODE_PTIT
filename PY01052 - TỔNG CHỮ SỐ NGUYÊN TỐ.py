from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def check(n):
    sum = 0
    for c in n:
        sum += ord(c) - ord('0')
    return snt(sum)

def main():
    n = input()
    print("YES" if check(n) else "NO")

for tc in range(int(input())):
    main()