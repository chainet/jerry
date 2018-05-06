def isRun(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False
def current_year_days(month, days, years):
    monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(month-1):
        days += monthlist[i]
    if month > 2 and isRun(years):
        days += 1
    return days


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
month = int(input())
print('请输入日期：')
days = int(input())

days = current_year_days(month, days, years)
run = 0
for i in range(1900, years, 4):
    if isRun(i):
        run += 1
ping = (years - 1900) - run
pastdays =((run * 366) + (ping * 365) + days) - 1
day = pastdays % 7
weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
print(weekday[day])