print("welcome to SBI bank")
swap=input("please insert your card")
if swap=="insert":
    print("remove your card")
    language=input("please select language")
    if language=="english":
        number=input("enter any number between 10 and 90 for eg.'25")
        pin=input("please enter your pin")
        if pin=="1234":
            print("pin is correct")
            trans=input("please select the transction")
            if trans=="fast cast" or trans=="withdrawal" or trans=="balence inquiry":
                account=input("please select account type")
                if account=="saving" or account=="current":
                    print("cash available-Rs 100,Rs 500,Rs 2000") 
                    amount=int(input("please enter amount"))
                    if amount<=20000:
                        print("your transaction is being processed. please Wait")
                    else:
                        print("amount is more than 20000")
                else:
                    print("invalid acount")
            else:
                print("invalid transection")
        else:
            print("ivalid pin")
    elif language=="hindi":
        number=input("10 ya 90 me se koe ek ank daliye")
        pin=input("krupaya aapka pin daliye")
        if pin=="1234":
            print("aapka pin sahi hai")
            trans=input("krupaya len den ka prakar batahye")
            if trans=="teji se nakdi" or trans=="nikasi" or trans=="balance puchtach":
                account=input("krupaya aapna khata prakar chuniye")
                if account=="bachat" or account=="chalu khata":
                    print("cash available-Rs100,200,500,2000")
                    amount=int(input("krupaya pese daliye"))
                    if amount<=20000:
                        print("aapka len den kriya suru hai thoda wait kare")
                    else:
                        print("pese 20000 se jyada hai")
                else:
                    print("khata sahi nahi hai")
            else:
                print("len den shahi nahi hai")
        else:
            print("pin sahi nahi hai")
    else:
        print("invalid language")
else:
    print("try again")

    
        
        
        
        

                                




        

                    

                        
                
                    
