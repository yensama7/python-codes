#This is a module for Bank_Account.py
class balanceException(Exception):
    pass

class bankAccount:
#creates the account
    def __init__(self, Acct_balance, Acct_name):
        self.name = Acct_name
        self.balance = Acct_balance
        print(f"\nAccount '{self.name}' created\nBalance = ${self.balance:.2f}")

#gets account balance
    def get_balance(self):
        print(f"\n'{self.name} Balance = ${self.balance :.2f}\n")

#Deposits into the account
    def deposit(self, Amount):
        self.balance = self.balance + Amount
        print("\nDeposit complete.........")
        self.get_balance()

#checks balance to know if the account is eligible for transaction
    def transaction_eligibility(self, Amount):
        if self.balance >= Amount :
            return
        else:
            raise balanceException(f"\nAccount '{self.name}' your Account balance is too low for this transaction")

#withdraws from the account
    def withdraw(self, Amount):
        try:
            self.transaction_eligibility(Amount)
            self.balance = self.balance - Amount
            print("\nWithdrawal complete..........")
            self.get_balance()

        except balanceException as error:
            print(f"Withdrawal stopped: {error}")
#transfers money from the account
    def trans(self, Amount, Account):
        self.balance = self.balance - Amount
        self.get_balance()
        print(f"Transfer to {Account} was successful")
        print("\n\n**********transfer complete**********")

    def transfer(self, Amount, Account):
        try:
            print("\n\n**********Begin transfer**********")
            self.transaction_eligibility(Amount)
            self.trans(Amount, Account)
        except balanceException as error:
            print(f"Transaction stopped: {error}")
#******************************************

#for savings account
class savings(bankAccount):
    def __init__(self, Acct_balance, Acct_name):
        super().__init__(Acct_balance, Acct_name) 
    
#Deposits to the account
    def deposit(self, Amount):
        self.balance = self.balance + (Amount * 1.05)
        print("\nDeposit complete.........")
        self.get_balance()
