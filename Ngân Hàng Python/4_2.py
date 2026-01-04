
n = int(input())
a = []

for _ in range(n):
    name = input()
    ns = input()
    m1, m2, m3 = float(input()), float(input()), float(input())
    
    minn = min(m1, min(m2, m3))
    
    if minn == m1:
        dtb = m1 * 2 + m2 + m3
    elif minn == m2:
        dtb = m1 + m2 * 2 + m3
    else: dtb = m1 + m2 + m3 * 2
    
    a.append([name, ns, dtb / 4])

for ts in sorted(a, key=lambda x: -x[2]):
    print(f"{ts[0]} {ts[1]} {ts[2]:.1f}")