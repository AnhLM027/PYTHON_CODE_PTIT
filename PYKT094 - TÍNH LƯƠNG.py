
class NV:
    def __init__(self, id, name, luongcb, ncong):
        self.id = id
        self.name = name
        
        mp = {
            "A": [10, 12, 14, 20],
            "B": [10, 11, 13, 16],
            "C": [9, 10, 12, 14],
            "D": [8, 9, 11, 13]
        }
        
        nhom = id[0]
        namct = int(id[1:3])
        self.idPhong = id[3:]
        
        if 1 <= namct <= 3: luong = luongcb * mp[nhom][0]
        elif 4 <= namct <= 8: luong = luongcb * mp[nhom][1]
        elif 9 <= namct <= 15: luong = luongcb * mp[nhom][2]
        else: luong = luongcb * mp[nhom][3]
        
        self.luong = luong * ncong

mp = {}
for _ in range(int(input())):
    s = input().split()
    mp[s[0]] = ' '.join(s[1:])

a = []
for _ in range(int(input())):
    a.append(NV(input(), input(), int(input()), int(input())))

for nv in a:
    print(f"{nv.id} {nv.name} {mp[nv.idPhong]} {nv.luong}000")