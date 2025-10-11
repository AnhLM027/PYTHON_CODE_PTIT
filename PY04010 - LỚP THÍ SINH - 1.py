
class SV:
    def __init__(self, name, age, m1, m2, m3):
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def hienthi(self):
        age = self.age
        if age[2] != '/': age = "0" + age
        if age[5] != '/': age = age[:5] + '/' + age[5:]
        td = self.m1 + self.m2 + self.m3
        print(self.name, age, f'{td:.1f}')

a = SV(input(), input(), float(input()), float(input()), float(input()))
a.hienthi()