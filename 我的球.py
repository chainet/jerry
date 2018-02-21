class ball:
    def __init__(self,color,size,direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce (self):
        if self.direction == '往下蹦':            
            self.direction = '往上蹦'

my_ball = ball('蓝色','小','往下蹦')
print ('我要创建一个球')

print ('我的球很' + my_ball.size + '。')
print ('我的球是' + my_ball.color + '的。')
print ('我的球正在' + my_ball.direction + '。')
print('现在我要去拍我的球了。', end='')
print('')
my_ball.bounce()
print('现在我的球正在' + my_ball.direction + '。')