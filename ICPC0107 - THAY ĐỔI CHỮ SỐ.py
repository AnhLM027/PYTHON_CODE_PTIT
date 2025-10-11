def cv(a, b, x):
    return int(x.replace(str(a), str(b)))

def main():
    a, b = [int(x) for x in input().split()]
    n1 = input()
    if len(n1.split()) > 1: n1, n2 = n1.split()
    else: n2 = input()
    if a > b: a, b = b, a
    print(cv(b, a, n1) + cv(b, a, n2), cv(a, b, n1) + cv(a, b, n2))

tc = int(input())
while tc > 0:
    tc -= 1
    main()