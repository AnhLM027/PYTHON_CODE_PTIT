
s = input()
t = ""
cnt = 0

for i in range(len(s) - 1, -1, -1):
    cnt += 1
    t += s[i]
    if cnt % 3 == 0 and cnt != len(s):
        t += ','

print(''.join(reversed(t)))