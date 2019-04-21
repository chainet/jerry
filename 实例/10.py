#实例10
#http://www.runoob.com/python/python-exercise-example10.html
import time
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))