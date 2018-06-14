print('6.小时&分钟')
print('输入分钟：')
enter_minute = int(input())
hour = int(enter_minute / 60)
minute = enter_minute % 60
print('结果是：%s时 %s分' % (hour, minute))

print('7.除法算式')
print('输入被除数：')
a = int(input())
print('输入除数：')
b = int(input())
answer_1 = int(a / b)
answer_2 = a % b
print('商是', answer_1, '余数是', answer_2)