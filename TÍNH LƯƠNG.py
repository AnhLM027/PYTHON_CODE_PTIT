

COEFF = {
    "A": {1: 10, 4: 12, 9: 14, 16: 20},
    "B": {1: 10, 4: 11, 9: 13, 16: 16},
    "C": {1: 9, 4: 10, 9: 12, 16: 14},
    "D": {1: 8, 4: 9, 9: 11, 16: 13},
}

class Department:
    def __init__(self, code, name):
        self.code, self.name = code, name

class Employee:
    def __init__(self, code, name, base, days, depts):
        self.code, self.name, self.base, self.days, self.depts = code, name, base, days, depts
        self.coeff = self.get_coeff()
        self.salary = self.base * self.days * self.coeff
    def get_coeff(self):
        k, y = self.code[0], int(self.code[1:3])
        key = 1 if y <= 3 else 4 if y <= 8 else 9 if y <= 15 else 16
        return COEFF[k][key]
    def __str__(self):
        return f"{self.code} {self.name} {self.depts[self.code[-2:]].name} {self.salary}000"

class Company:
    def __init__(self):
        self.depts, self.emps = {}, []
    def add_dept(self, c, n): self.depts[c] = Department(c, n)
    def add_emp(self, c, n, b, d): self.emps.append(Employee(c, n, b, d, self.depts))
    def show(self): [print(e) for e in self.emps]

def main():
    c = Company()
    for _ in range(int(input())):
        x, y = input().split(maxsplit=1)
        c.add_dept(x, y)
    for _ in range(int(input())):
        c.add_emp(input().strip(), input().strip(), int(input()), int(input()))
    c.show()

if __name__ == "__main__":
    main()
