n=int(float(input("enter time")))
if n<=5:
    print("sleeping time")
elif n>5 and n<=7:
    print("morning excercise")
elif n>7 and n<9:
    print("doing your work")
elif n>=9 and n<=10:
    print("english activity")
elif n>10 and n<=13:
    print("coding time")
elif n>13 and n<=14.30:
    print("lunch time")
elif n>=14.30 and n<=17:
    print("coding time")
elif n>17 and n<=17.30:
    print("break time")
elif n>17.30 and n<=19:
    print("culture activity")
elif n>19 and n<=21:
    print("coding time")
elif n>21 and n<=22:
    print("dinner time")
elif n>22:
    print("go to bed")
else:
    print("invalid time")