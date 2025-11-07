
class Player:
    def __init__(self, id, name, vao, ra):
        self.id = id
        self.name = name
        h1, m1 = map(int, vao.split(":"))
        h2, m2 = map(int, ra.split(":"))
        self.time = h2 * 60 + m2 - h1 * 60 - m1
        self.gio = self.time // 60
        self.phut = self.time % 60
        
    def __str__(self):
        return f"{self.id} {self.name} {self.gio} gio {self.phut} phut"
    
a = []
for i in range(1, int(input()) + 1):
    a.append(Player(input(), input(), input(), input()))
    
for pl in sorted(a, key=lambda x: (-x.time)):
    print(pl)