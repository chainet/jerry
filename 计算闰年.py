def s(start,end):
   a=0
   b=0
   for year in range(start,end+1):
       if (year%4==0 and year%100!=0) or (year%400==0):
           a+=1
       else:
           b+=1
   return(a,b)

def isRun(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False

