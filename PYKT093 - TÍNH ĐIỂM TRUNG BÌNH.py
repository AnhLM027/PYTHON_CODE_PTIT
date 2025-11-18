
class SV:
    def __init__(self, id, name, diem):
        self.id = f"SV{id:02d}"
        self.name = name
        self.diem = diem

    def __str__(self):
        return f"{self.id} {self.name} {self.diem:.2f}"

def chuanhoa(s):
    arr = s.split()
    res = [(t[0].upper() + t[1:].lower()) for t in arr]
    return ' '.join(res)

n = int(input())
a = []
idx = 1
for i in range(1, n + 1):
    name = chuanhoa(input().strip())
    arr = [int(input()) for _ in range(3)]
    diem = arr[0] * 3 + arr[1] * 3 + arr[2] * 2
    tb = round(diem / 8 + 1e-9, 2)
    a.append(SV(i, name, tb))

a.sort(key=lambda x: (-x.diem, x.id))

cur = 0.0
rank, cnt = 1, 0

for sv in a:
    print(sv, end=' ')
    if sv.diem == cur: cnt += 1
    else:
        rank += cnt
        cnt = 1
    cur = sv.diem
    print(rank)
        
