
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(' '.join(map(str, sorted(a & b))))
print(' '.join(map(str, sorted(a - b))))
print(' '.join(map(str, sorted(b - a))))