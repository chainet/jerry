print('6.小时&分钟')
print('输入分钟：')
enter_minute = int(input())
hour = int(enter_minute / 60)
minute = enter_minute % 60
print('结果是：%s时 %s分' % (hour, minute))

print('7.除法算式')
print('输入被除数：')
A = int(input())
print('输入除数：')
B = int(input())
answer_1 = int(A / B)
answer_2 = A % B
print('商是', answer_1, '余数是', answer_2)

print('8.abc交换')
print('输入a：')
a = int(input())
print('输入b：')
b = int(input())
print('输入c：')
c = int(input())
d = 0
d = a
a = b
b = c
c = d
print('a = ', a, 'b = ', b, 'c = ', c,)

print('9.比大小')
print('输入x：')
x = int(input())
print('输入y：')
y = int(input())
if x > y:
    print('大数是：', x)
elif x < y:
    print('大数是：', y)
else:
    print('ERROR!!!!!')