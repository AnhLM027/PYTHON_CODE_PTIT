
def main():
    n, d = map(int, input().split())
    a = input().split()
    print(' '.join(a[d:] + a[:d]))

tc = int(input())
while tc > 0:
    tc -= 1
    main()