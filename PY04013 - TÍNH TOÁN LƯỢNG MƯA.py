
class Tram:
    def __init__(self, name, ma):
        self.name = name
        self.ma = "T"
        if ma <= 9: self.ma += "0" + str(ma)
        else: self.ma += str(ma)
        self.time = 0
        self.total = 0

    def update(self, st, en, k):
        self.time += int(en[:2]) * 60 + int(en[3:]) - (int(st[:2]) * 60 + int(st[3:]))
        self.total += k
    
    def __str__(self):
        return f"{self.ma} {self.name} {self.total / self.time * 60:.2f}"
    

n = int(input())
a = {}
cnt = 1

for _ in range(n):
    name = input().strip()
    st, en = input(), input()
    k = int(input())
    if name not in a:
        a[name] = Tram(name, cnt)
        cnt += 1
    a[name].update(st, en, k)

# a = sorted(a.values(), key = lambda x: x.name)
for tram in a.values():
    print(tram)