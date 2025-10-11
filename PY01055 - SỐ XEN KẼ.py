
def main():
    n = input()
    if len(n) % 2 == 0 or n[0] == n[1]: return False
    c = n[0]
    for i in range(0, len(n), 2):
        if c != n[i]: return False
    return True
    

for tc in range(int(input())):
    print("YES" if main() else "NO")