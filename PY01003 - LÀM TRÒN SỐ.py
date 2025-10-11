import math

def main():
    n = input()
    i = 1
    m = float(n)
    l = len(n)
    for i in range(l):
        # print(m / pow(10, i), round(m / pow(10, i)))s
        m = round(m / pow(10, i) + 1e-9) * pow(10, i)
    print(m)

for tc in range(int(input())):
    main()