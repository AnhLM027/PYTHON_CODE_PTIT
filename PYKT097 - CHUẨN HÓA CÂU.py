
lines = []
for _ in range(100):
    try:
        line = input()
        if line.strip() == "": continue
        lines.append(line.strip())
    except EOFError:
        break
    
for line in lines:
    l = line.lower().split()
    t = ' '.join(l)
    while t[-2] == ' ':
        t = t[:-2] + t[-1]
    print(t[0].upper() + t[1:] + ("." if t[-1] not in ".!?" else ""))