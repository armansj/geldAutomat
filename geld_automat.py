
def z_bank():
    
    z_bank_profit=0.96
    def withdraw():

       new_amount=0
       withdrawal=float(input("please enter how many geld you want give from your account: \t"))
       new_amount=current_amount-withdrawal
       if new_amount<0:
         print(f"you money is less than {withdrawal}")
       print(f"your new amount is : \t {new_amount*z_bank_profit}")
       with open("saver.txt",'w',encoding = 'utf-8') as file:
            file.write(f"new Amount After Withdraw : {new_amount*z_bank_profit}\n")

    def deposit():

        deposit=float(input("please enter how much you want put in your account: \t"))
        new_amount=current_amount+deposit
        
        
        print(f"your final amount is:\t {new_amount*z_bank_profit}")
        with open("saver.txt",'w',encoding = 'utf-8') as file:
            file.write(f"new Amount After Deposit : {new_amount*z_bank_profit}\n")



    print("welcome to ziraat bank!\n")
    print("vorsicht your transactron with this card have 4% profit for atm")
    pass_code=int(input("please enter your pass: \t"))


    
    if pass_code==1111:
        
        print("great password is currect \n")
        print("welcome to our bank")
        while True:
            current_amount=float(input("please enter your account amount: \t"))
            ask_for_withraw_or_deposit=input("please enter do you want widthraw or deposit? : \t(w widraw / d for deposit)\t")
            if ask_for_withraw_or_deposit=='w':
                print("you want to widthraw!")
                withdraw()
            elif ask_for_withraw_or_deposit=='d':
                print("you want to deposit!")
                deposit()
    else:
        
        print(f"pass is wrong Try again ")
        z_bank()




def s_bank():
    s_bank_profit=0
    def withdraw():
    
       new_amount=0
       withdrawal=float(input("please enter how many geld you want give from your account: \t"))
       new_amount=current_amount-withdrawal
       if new_amount<0:
         print(f"you money is less than {withdrawal}")
       print(f"your new amount is : \t {new_amount}")
       with open('saver.txt', 'w') as file:
            file.write(f"my new amount After Withdraw {new_amount}\n")
       

    def deposit():

        deposit=float(input("please enter how much you want put in your account: \t"))
        new_amount=current_amount+deposit
        print(f"your final amount is:\t {new_amount}")
        with open('saver.txt', 'w') as file:
            file.write(f"my new amount After deposit {new_amount}\n")
        



    print("welcome to sparkasse bank!\n")
    print("vorsicht your transactron with this card have 0% profit for atm")


    pass_code=int(input("please enter your pass: \t"))


    
    if pass_code==2222:
        print("great password is currect \n")
        print("welcome to Sparkasse bank")
        while True:
            current_amount=float(input("please enter your account amount: \t"))
            ask_for_withraw_or_deposit=input("please enter do you want widraw or deposit? : \t(w widraw / d for deposit)\t")
            if ask_for_withraw_or_deposit=='w':
                print("you want to widraw!")
                withdraw()
            elif ask_for_withraw_or_deposit=='d':
                print("you want to deposit!")
                deposit()
    

    else:
        print("pass is wrong Try again")
        s_bank()







card_holder=input("please enter you cardholder Bank:(s,z) : \t")

if card_holder=='z':
    z_bank()

    




elif card_holder=='s':
    s_bank()
    

            

        
        
    
    
    

    

        
        


        




