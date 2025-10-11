from math import sqrt

def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def main():
    n = input()
    sum = 0
    for i in range(0, len(n), 1):
        sum += int(n[i])
        if (int(n[i]) - i) & 1: return False
    return snt(sum)
    

for tc in range(int(input())):
    print("YES" if main() else "NO")