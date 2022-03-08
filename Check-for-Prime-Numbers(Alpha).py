print("请输入一个大于等于2的整数！（输入其他字符即可结束运行）\n")

while 1:
        c=1
        k=1
        
        try:
             n=int(input())
        except:
            break
        else:
            
            if n<1:
                print("输入不合法！")
                continue
            if n==1:
                print("1既不是质数也不是合数！")
                continue
            if n==2:
                print("2是质数!")
                continue
            if n==3:
                print("3是质数!")
                continue
            if n%2==0:
                print(n,"是合数，因为它可以被2整除")
                continue
            if n%3==0:
                print(n,"是合数，因为它可以被3整除")
                continue
            while (n/(6*k-1))>=(6*k-1) or (n/(6*k+1))>=(6*k+1):
                if n%(6*k-1)==0:
                    print(n,"是合数，因为它可以被",6*k-1,"整除")
                    c=2
                    break
                if n%(6*k+1)==0:
                    print(n,"是合数，因为它可以被",6*k+1,"整除")
                    c=2
                    break
                k+=1
            if c==1:
                 print(n,"是质数！")
                 continue
      

    
print("\n感谢您的使用！")
