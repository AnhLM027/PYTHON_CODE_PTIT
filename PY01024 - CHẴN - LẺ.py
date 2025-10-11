from math import sqrt

def sub(a, b):
    return ord(a) - ord(b)
def main():
    n = input()
    sum = sub(n[0], '0')
    check = True
    for i in range(1, len(n), 1):
        if abs(sub(n[i], n[i - 1])) != 2:
            check = False
            break
        sum += sub(n[i], '0')
    
    print("YES" if (check and sum % 10 == 0) else "NO")

for tc in range(0, int(input())):
    main()