
class MH:
    def __init__(self, id, name, sl, gia, ck):
        self.id = id
        self.name = name.strip()
        self.sl = int(sl)
        self.gia = int(gia)
        self.ck = int(ck)
        self.cost = self.sl * self.gia - self.ck

    def __str__(self):
        return f"{self.id} {self.name} {self.sl} {self.gia} {self.ck} {self.cost}"

n = int(input())
a = []
for i in range(1, n + 1):
    a.append(MH(input(), input(), input(), input().strip(), input().strip()))

for mh in sorted(a, key=lambda x: -x.cost):
    print(mh)
