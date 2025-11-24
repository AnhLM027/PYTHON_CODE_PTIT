
res = []
with open('SOTAY.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
i = 0
while i < len(lines):
    if lines[i].startswith("Ngay"):
        date = lines[i].split()[1]
        i += 1
        continue
    name = lines[i]
    phone = lines[i + 1]
    res.append((name, phone, date))
    i += 2

def cmp(arr):
    parts = arr[0].split()
    return (parts[-1], ' '.join(parts[:-1]))

res.sort(key=cmp)

for name, phone, date in res:
    print(f"{name}: {phone} {date}")