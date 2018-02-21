import my_module

celsius = int(input('输入摄氏温度：'))
fahrenheit = my_module.c_to_f(celsius)
print('转换后的华氏温度是：', fahrenheit)