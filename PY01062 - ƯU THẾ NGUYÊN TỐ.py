from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def check(n):
    if not snt(len(n)): return False
    cnt = 0
    for c in n:
        if snt(int(c)): cnt += 1
    return cnt > len(n) - cnt

def main():
    n = input()
    print("YES" if check(n) else "NO")

for tc in range(int(input())):
    main()