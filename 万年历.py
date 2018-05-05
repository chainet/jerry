from 计算闰年 import isRun

print('请输入年份（必须是1900年到2099年）：')
years = int(input())
if years < 1900 or years > 2099:
    print('错误')
    exit()
if isRun(years):
    print("闰年")
else:
    print('平年')
print('请输入月份：')
month = input()
print('请输入日期：')
days = int(input())

one = 31
two = 28
three = 31
four = 30
five = 31
six = 30
seven = 31
eight = 31
nine = 30
ten = 31
eleven = 30
twelve = 31

for i in range(1,2):
    if month == '1':
        days = days
    elif month == '2':
        days += one
    elif month == '2' and isRun(years):
        days += one + 1
    elif month == '3':
        days += one + two
    elif month == '4':
        days += one + two + three
    elif month == '5':
        days += one + two + three + four
    elif month == '6':
        days += one + two + three + four + five
    elif month == '7':
        days += one + two + three + four + five + six
    elif month == '8':
        days += one + two + three + four + five + six + seven
    elif month == '9':
        days += one + two + three + four + five + six + seven + eight
    elif month == '10':
        days += one + two + three + four + five + six + seven + eight + nine
    elif month == '11':
        days += one + two + three + four + five + six + seven + eight + nine + ten
    elif month == '12':
        days += one + two + three + four + five + six + seven + eight + nine + ten + eleven
    else:
        print('错误')
        exit()

run = 0
for i in range(1900, years, 4):
    if isRun(i):
        run += 1
ping = (years - 1900) - run
pastdays =((run * 366) + (ping * 365) + days)
day = (pastdays + days) % 7
weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
print(weekday[day])