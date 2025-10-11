
def sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def main():
    n, a = int(input()), list(map(int, input().split()))
    a = sorted(a, key = lambda x : (sum(x), x))
    print(*a)

for tc in range(int(input())):
    main()