from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def main():
    n = input()
    print("YES" if snt(int(n[-4:])) else "NO")

for tc in range(int(input())):
    main()