a=int(input("first side of tringle"))
b=int(input("second side of tringle"))
c=int(input("third side of tringle"))
n=180
if (a==b==c) and (n==a+b+c):
    print("equilateral")
elif (a==b or b==c or c==a) and (n==a+b+c):
    print("isoseclence")
elif (a!=b!=c) and (n==a+b+c):
    print("scalene")
else:
    print("it is not tringle")