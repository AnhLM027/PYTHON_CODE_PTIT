
def chuan_hoa_ten(ten: str):
    return ' '.join(word.capitalize() for word in ten.strip().lower().split())

def tinh_uu_tien(dtoc, kv):
    res = 0.0
    if kv == '1':
        res += 1.5
    elif kv == '2':
        res += 1.0
    
    if dtoc.lower() != 'kinh':
        res += 1.5
    return res

class ThiSinh:
    def __init__(self, ma, ten, diem, dtoc, kv):
        self.ma = f"TS{ma:02d}"
        self.ten = chuan_hoa_ten(ten)
        self.diem = float(diem)
        self.res = tinh_uu_tien(dtoc, kv)
        self.tong = self.diem + self.res
        self.tt = "Do" if self.tong >= 20.5 else "Truot"

    def __repr__(self):
        return f"{self.ma} {self.ten} {self.tong:.1f} {self.tt}"

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    diem = float(input().strip())
    dtoc = input().strip()
    kv = input().strip()
    ds.append(ThiSinh(i, ten, diem, dtoc, kv))

ds.sort(key=lambda x: (-x.tong, x.ma))

for ts in ds:
    print(ts)
