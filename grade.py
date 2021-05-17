# a=int(input("selling price"))
# b=int(input("cost price"))
# if a>b:
#     print(a-b,"profit")
# elif a<b:
#     print(b-a,"loss")
# elif a==b:
#     print("no profit no loss")
# else:
#     print("rest of of the code")
    
# physics=int(input("enter marks"))
# chemistry=int(input("enter marks"))
# biology=int(input("enter marks"))
# maths=int(input("enter marks"))
# computer=int(input("enter marks"))
# vn=(physics+chemistry+biology+maths+computer)/5
# if vn>=90:
#     print("Grade A")
# elif vn>=80:
#     print("Grade B")
# elif vn>=70:
#     print("Grade C")
# elif vn>=60:
#     print("Grade D")
# elif vn>=40:
#     print("Grade E")
# elif vn>30<40:
#     print("Grade F")
# else:
#     print("fail")



# vn=int(input("enter units"))
# if vn>=1 and vn<=50:
#     print(0.50*vn)
# elif vn>=50 and vn<=150:
#     print(0.75*vn)
# elif vn>=150 and vn>=250:
#     print(1.20*vn)
# else:
#     print(1.50*vn)


n=int(input("enter 1st person age"))
x=int(input("enter 2nd person age"))
y=int(input("enter 3rd person age"))
if n>x>y:
    print(y,"yongest", x,"oldest than", n,"oldest")
elif n>y>x:
    print(x, "youngest", y,"oldest than 2nd person", n,"oldest")
elif x>y>n:
    print(n,"youngest", y,"oldest than 1st person", x,"oldest")
elif x>n>y:
    print(y,"youngest",n,"oldest than 3rd person", x,"oldest")
elif n<x<y:
    print(n, "youngest", x,"oldest than 1st person", y,"oldest")
elif x<n<y:
    print(x,"youngest", n,"oldest than 2nd perosn", y,"oldest")
else:
    print("all are same")
