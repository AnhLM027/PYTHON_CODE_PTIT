
def tn(s):
    if len(s) <= 1: return False
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True

def check(n):
    sum = 0
    for c in n:
        sum += ord(c) - ord('0')
    return tn(str(sum))

def main():
    n = input()
    print("YES" if check(n) else "NO")

for tc in range(int(input())):
    main()