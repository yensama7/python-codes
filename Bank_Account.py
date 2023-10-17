from Bank_account_module import *
#welcome**********************************************************************************
def name():
    print("vault bank".center(50,"*"))
    print("Welcome to Vault bank, Please create an account")
    f_Name = input("\nplease input your First Name\n")
    l_Name = input("\nplease input your Last Name\n")
    full_name = f"{f_Name} {l_Name}"
    print("\nWelcome ", full_name)
    money = 0
    Pin = input("\nCreate a secret pin: ")
    welcome_back = False
#***************************************************************************************

#Savings account*********************************************************************************
    def acct_creation():
        acct = savings(money,full_name)
        def savings_acct(full_name):
            nonlocal welcome_back
            nonlocal acct_creation
            if welcome_back == True:
                print(f"\nWelcome back {full_name}")
            print("\nWould you like to Deposit, Transfer or withdraw? ")
            DTW = input("\nEnter\n1 to Deposit\n2 to transfer\n3 to Withdraw\n")
            if DTW not in ["1", "2", "3"]:
                print("\nPlease enter 1, 2 or 3\n")
                welcome_back = True
                return savings_acct(full_name)
    #deposit******************************************************
            if DTW == "1":
                deposit_money = input("\nEnter the amount you want to deposit into the bank: $")
                try:
                    dm = int(deposit_money)
                except:
                    print("\nInput amount in digits")
                    welcome_back = True

                    return savings_acct(full_name)
                    quit()
                acct.deposit(dm)
                welcome_back = True
                return savings_acct(full_name)
    #transfer*******************************************************
            elif DTW == "2":
                how_much = input("\nHow much would you like to transfer: $")
                try:
                    hm = int(how_much)
                except:
                    print("\nInput amount in digits")
                    welcome_back = True

                    return savings_acct(full_name)
                    quit()
                transferee = input("\nwho do you wish to transfer to: ")
                enter_pin = input("\nEnter pin: ")
                if enter_pin == Pin:
                    acct.transfer(hm,transferee)
                    welcome_back = True

                    return savings_acct(full_name)
                else:
                    print("\nwrong pin")
                    welcome_back = True

                    return savings_acct(full_name)
    #Withdraw***********************************************************
            else:
                how_much = input("\nHow much would you like to withdraw: $") 
            try:
                hm = int(how_much)
            except:
                print("\nInput amount in digits")
                welcome_back = True
                return savings_acct(full_name)
                quit()
            enter_pin = input("\nEnter pin: ")
            if enter_pin == Pin:
                acct.withdraw(hm)
                welcome_back = True
                return savings_acct(full_name)
            else:
                print("\nWrong pin")
                welcome_back = True
                return savings_acct(full_name)
        savings_acct(full_name)
    #*********************************************************************************************

#Current account******************************************************************************
    def Current_acct():
        acct = bankAccount(money,full_name)
        def Current(full_name):
            nonlocal welcome_back
            nonlocal Current_acct
            if welcome_back == True:
                print(f"\nWelcome back {full_name}")
            print("\nWould you like to Deposit, Transfer or withdraw? ")
            DTW = input("\nEnter\n1 to Deposit\n2 to transfer\n3 to Withdraw\n")
            if DTW not in ["1", "2", "3"]:
                print("\nPlease enter 1, 2 or 3\n")
                welcome_back = True
                return Current(full_name)
    #deposit******************************************************
            if DTW == "1":
                deposit_money = input("\nEnter the amount you want to deposit into the bank: $")
                try:
                    dm = int(deposit_money)
                except:
                    print("\nInput amount in digits")
                    welcome_back = True
                    return Current(full_name)
                    quit()
                acct.deposit(dm)
                welcome_back = True
                return Current(full_name)
    #transfer*******************************************************
            elif DTW == "2":
                how_much = input("\nHow much would you like to transfer: $")
                try:
                    hm = int(how_much)
                except:
                    print("\nInput amount in digits")
                    welcome_back = True
                    return Current(full_name)
                    quit()
                transferee = input("\nwho do you wish to transfer to: ")
                enter_pin = input("\nEnter pin: ")
                if enter_pin == Pin:
                    acct.transfer(hm,transferee)
                    welcome_back = True
                    return Current(full_name)
                else:
                    print("\nwrong pin")
                    welcome_back = True
                    return Current(full_name)
    #Withdraw***********************************************************
            else:
                how_much = input("\nHow much would you like to withdraw: $") 
            try:
                hm = int(how_much)
            except:
                print("\nInput amount in digits")
                welcome_back = True
                return Current(full_name)
                quit()
            enter_pin = input("\nEnter pin: ")
            if enter_pin == Pin:
                acct.withdraw(hm)
                welcome_back = True
                return Current(full_name)
            else:
                print("\nWrong pin")
                welcome_back = True
                return Current(full_name)
        Current(full_name)
#***********************************************************************************************
           
#USer interface*************************************************************************
    def UI():
        print("Would you like to Create Savings Account or Current Account")
        choice = input("\nEnter\n1 for Savings Account\n2 for Current Account\n")
        if choice not in ["1", "2"]:
            print("\nPlease enter 1 or 2\n")
            return UI()
        if choice == "1":
            acct_creation()
        elif choice == "2" :
            Current_acct()
#***************************************************************************************
    UI()
name()