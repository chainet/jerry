print('1.求长方形面积')
print('输入长：')
width = int(input())
print('输入宽：')
high = int(input())
answer_1 = width * high
print('答案是：', answer_1)

print('2.求圆形面积')
print('输入半径：')
radius = int(input())
circumference_rate = 3.1415926
answer_2 = circumference_rate * radius * radius
print('答案是：', answer_2)

print('3.求A，B，C的值')
print('输入A：')
A = input()
print('输入B：')
B = input()
print('输入C：')
C = input()
print('A = ' + A, '   B = ' + B, '   C = ' + C)

print('4.交换x和y，求出它们')
print('输入x：')
x = input()
print('输入y：')
y = input()
z = 0
z = y
y = x
x = z
str(x)
str(y)
print('x = ' + x, '   y = ' + y)