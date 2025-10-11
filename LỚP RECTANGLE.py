
class Rectangle:
    def __init__(self, x, y, cl: str):
        self.x = x
        self.y = y
        self.cl = cl
    def perimeter(self):
        return (self.x + self.y) * 2
    def area(self):
        return self.x * self.y
    def color(self):
        return self.cl[:1] + self.cl[1:].lower()
    
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))