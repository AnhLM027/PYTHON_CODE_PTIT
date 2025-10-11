
cnt = 0

def sumOfDigits(s):
    if len(s) == 1: return
    global cnt
    cnt += 1

    tmp = 0
    for i in s: tmp += ord(i) - ord('0')
    sumOfDigits(str(tmp))

s = input().strip()
if len(s) <= 1: print(1)
else:
    sumOfDigits(s)
    print(cnt)