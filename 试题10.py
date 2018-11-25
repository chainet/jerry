print('10.可否被3整除?')
print('输入数字：')
num = int(input())
if num % 3 == 0:
    print('Yes!!!')
else:
    print('NO!!!')

print('11.咱班成绩')
print('输入你的成绩：')
Your_score = int(input())
if Your_score == 100:
    Level = 'A+'
elif 90 <= Your_score < 100:
    Level = 'A'
elif 80 <= Your_score < 90:
    Level = 'B'
elif 70 <= Your_score < 80:
    Level = 'C'
elif 60 <= Your_score < 70:
    Level = 'D'
elif Your_score < 60:
    Level = 'E'
else:
    print('ERROR!!!!!')
print('你的等级是：', Level)
# 方法二
# li = ['E', 'D', 'C', 'B', 'A']
# index = (Your_score - 60) // 10
if Your_score==100:
    index[]
# print(li[index])

