num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
symbol=input("enter symbol")
if symbol=="+":
    print(num1+num2)
elif symbol=="-":
    print(num1-num2 or num2-num1)
elif symbol=="*":
    print(num1*num2)
elif symbol=="/":
    print(num1/num2)
elif symbol=="%":
    print(num1%num2)
elif symbol=="**":
    print(num1**num2)
elif symbol=="//":
    print(num1//num2)
else:
    print("incorect symbol")

    
            


