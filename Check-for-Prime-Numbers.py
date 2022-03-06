import sys

a=1
b=1
k=1

while a==1:
  while b==1:
    n=float(input("请输入一个大于等于2的整数:"))
    if n<1:
      print("输入不合法！")
      break
    if n==1:
      print("1既不是质数也不是合数！")
      break
    if n==2:
      print("2是质数!")
      break
    while (n/(6*k-1))<(6*k-1) or (n/(6*k+1))<(6*k+1):
      if n%(6*k-1)==0:
        print(n,"是合数，因为它可以被",6*k-1,"整除")
        break
      if n%(6*k+1)==0:
        print(n,"是合数，因为它可以被",6*k+1,"整除")
        break
      k+=1
    print(n,"是质数！")
  a=float(input("是否继续？（1.是 2.否）"))
  
print("感谢您的使用！")
sys.exit(0)
