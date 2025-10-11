
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    a.sort(), b.sort()
    while i < n and a[i] <= b[i]: i += 1
    return i == n

for tc in range(0, int(input())):
    print("YES" if main() else "NO")