
def main():
    n = input()
    tong, tich = 0, 1
    check = False
    for i in range(0, len(n), 1):
        if i & 1:
            if n[i] != '0': 
                check = True
                tich *= int(n[i])
        else: tong += int(n[i])
    print(f"{tong} {tich if check else 0}")

for tc in range(0, int(input())):
    main()