print('输入数字：')
maxium = int(input())
begin = 1
number = 1
print(begin)
print(number)
while number < maxium:
    number = begin + number
    begin = number - begin
    if number >= maxium:
        break
    print(number)