


def rotate(s):
    k = sum(ord(c) - 65 for c in s)
    return ''.join(chr((ord(c) - 65 + k) % 26 + 65) for c in s)

def solve(s):
    n = len(s) // 2
    a, b = rotate(s[:n]), rotate(s[n:])
    return ''.join(chr((ord(a[i]) - 65 + ord(b[i]) - 65) % 26 + 65) for i in range(n))

for _ in range(int(input())):
    print(solve(input().strip()))
