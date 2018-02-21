import easygui

t = 0
while t < 6:
    f = easygui.enterbox('请输入密码：')
    t = t + 1
    if f == '20071102':
        easygui.msgbox ('您已进入。')
    elif f != '20071102':
        easygui.msgbox ('密码错误，请重试。')
    if t == 6:
        easygui.msgbox('您已经六次输入错误，请1分钟后再试。')
import time
for i in range (60,0,-1):
    print (i)
    time.sleep(1)
easygui.msgbox('时间已到，您可以再次输入密码')
