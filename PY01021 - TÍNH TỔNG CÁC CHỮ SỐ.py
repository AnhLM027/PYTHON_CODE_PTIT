
for _ in range(int(input())):
    s = input().strip()
    sum = 0
    ans = ''
    for i in range((len(s))):
        if s[i].isdigit(): sum += int(s[i])
        else: ans += s[i]
    ans = ''.join(sorted(ans, key = lambda x: x))
    print(ans + str(sum))