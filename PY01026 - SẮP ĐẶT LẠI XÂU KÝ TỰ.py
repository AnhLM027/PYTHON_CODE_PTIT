
for i in range(int(input())):
    s1, s2 = input(), input()
    print(f"Test {i + 1}:", "YES" if ''.join(sorted(s1)) == ''.join(sorted(s2)) else "NO")