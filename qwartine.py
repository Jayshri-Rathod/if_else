day=input("enter day")
x=input("take permision to disco")
if day=="sunday" and x=="yes":
    print("you can go out")
    y=input("going reason")
    if y=="hospital" or y=="personal work":
        print("mask and sanitizer is compolsay")
        print("you have to be qwartine for 7days")
        z="qwartine"
        if z=="qwartine":
            print("you have to use mask and sanitizer")
            print("you will be in seperate room and not come out from room")
            a=input("enter time")
            if a>"6pm":
                print("you will get oil")
            else:
                print("not get oil")
        else:
            print("no need to use")
    elif y=="ng works":
        print("use mask and sanitizer")
        print("you don't have to quartine")
        a=input("enter time")
        if a>"6pm":
            print("you will be quartine")
        else:
            print("not wiil be in quartine")
    else:
        print("can not in qwartine")    
else:
    print("can not go out")