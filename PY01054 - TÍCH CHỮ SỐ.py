
def main():
    n = input()
    tich = 1
    for c in n:
        if c != '0': tich *= int(c)
    print(tich)

for tc in range(int(input())):
    main()