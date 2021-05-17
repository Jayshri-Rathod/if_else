vn=int(input("enter year")
if vn%4==0:
    print("leap year")
    if vn%400==0:
        print("leap year")
        if vn%100==0:
            print("leap year")
else:
    print("not leap year")