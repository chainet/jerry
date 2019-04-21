#实例1 
#http://www.runoob.com/python/python-exercise-example1.html
for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            if i != k and i != j and j != k:
                print (i,j,k)