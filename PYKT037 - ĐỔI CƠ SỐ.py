
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cv(n, b):
    if n == 0: return "0"
    res = []
    while n > 0:
        res.append(digits[n % b])
        n //= b
    return "".join(reversed(res))

for _ in range(int(input())):
    n, b = map(int, input().split())
    print(cv(n, b))
