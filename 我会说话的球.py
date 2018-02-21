class ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
        
    def __str__(self):
        mag = '你好，我是个' + self.size + '的，' + self.color + '的球。'
        return mag
my_ball = ball('红色', '小小', '往下蹦')
print(my_ball)