#Test for composite numbers around 6

import sys

a=float(input("请输入起始值："))
b=float(input("请输入终点值："))

n=a

while n<=b: 
    if (6*n-1)%5==0 or (6*n-1)%7==0:
        if (6*n+1)%5==0 or (6*n+1)%7==0:
            print(6*n-1,6*n+1)
            n+=1
        else:
            n+=1
    else:
        n+=1

if n==b:
    print("检索完毕")
    sys.exit(0)
    
