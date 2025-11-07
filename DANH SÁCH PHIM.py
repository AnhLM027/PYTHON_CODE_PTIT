from datetime import datetime

n, m = map(int, input().split())
tl = {}

for i in range(1, n + 1):
    tl[f"TL{i:03}"] = input().strip()

films = []
for i in range(1, m + 1):
    ma_tl = input().strip()
    ngay = input().strip()
    ten = input().strip()
    tap = int(input().strip())
    d = datetime.strptime(ngay, "%d/%m/%Y")
    films.append((d, ten, -tap, f"P{i:03}", ten, tl[ma_tl], ngay, tap))

films.sort()

for f in films:
    print(f"{f[3]} {f[5]} {f[6]} {f[4]} {f[7]}")
