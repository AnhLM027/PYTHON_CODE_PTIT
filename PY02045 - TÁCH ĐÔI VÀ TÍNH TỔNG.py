
def sumOfDigits(s):
    if len(s) == 1: return 
    i = int(len(s) / 2)
    sum = int(s[0:i]) + int(s[i:])
    print(sum)
    sumOfDigits(str(sum))

s = input()
sumOfDigits(s)

