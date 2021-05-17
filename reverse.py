n=int(input("enter the number"))
x=n%10
y=(n//10)%10
z=((n//10)//10)%10
b=((n//10)//10)//10
a=x*1000+y*100+z*10+b
if a<100000:
    print(a)
else:
    print("input is wrong")
