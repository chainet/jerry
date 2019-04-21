#实例8
#http://www.runoob.com/python/python-exercise-example8.html
for i in range (1, 10):
    print
    for j in range (1, i + 1):
        # print ('%d*%d=%d'%(i, j, i*j))
        print(f'{i}*{j}={i*j}')