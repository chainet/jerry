class triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height / 2
        return area

class square:
    def __init__(self, size):
        self.size = size
    
    def get_area(self):
        area = self.size * self.size
        return area
class rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length
    
    def get_area(self):
        area = self.width * self.length
        return area
print('输入三角形的宽：')
a = int(input())
print('输入三角形的高：')
b = int(input())
mytriangle = triangle(a, b)
print('三角形面积为', mytriangle.get_area())
print('输入正方形的边长：')
c = int(input())
mysquare = square(c)
print('正方形面积为', mysquare.get_area())
print('输入长方形的长：')
d = int(input())
print('输入长方形的宽：')
e = int(input())
myrectangle = rectangle(d, e)
print('长方形面积为', myrectangle.get_area())