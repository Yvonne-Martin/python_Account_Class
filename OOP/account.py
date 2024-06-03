class Account:
    def __init__(self,number,pin):
        self.number=number
        self.__pin=pin
        self.__balance=0
    def show_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        else:
            return "wrong Pin"
    def deposit(self,amount):
        self.amount=amount
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        self.amount=amount
        self.__balance-=amount
        print(self.__balance)
    def view_account_details(self,name):
        print(f"Dear owner of account {self.number} {name} your account balance is Kshs.{self.__balance}")
    def update_account(self,number,name):
        print(f"Dear {name} your new account number is {number}")
    # def recent_transactions(self,name):
    #     print(f"Dename} your new account number is {number}")
    # def recent_transactions(self,name):
    #     print(f"Dear {name} you have deposited {self.amount} and withdrawn {self.amount}")
    def generate_statement(self,date):
      print(f"On {date} you withdrew {self.withdraw} and deposited {self.deposit}")
    
    def overdraft_limit(self,overdraft):
        self.overdraft=overdraft
        if self.__balance>overdraft:
            print(self.withdraw())
        else:
            print("you have insufficient funds. Please top up")
    def interest (self,interest_rate):
        self.interest_rate=interest_rate
        total_interest=self.balance*(interest_rate/100)
        print (total_interest)

    def apply_interest(self,rate):
        interest=self.interest(rate)
        self.__balance+=interest
        print (f"the new balance is {self.__balance}")

    def freeze(self):
        self.freeze=True
        print("your account is frozen") 

    def unfreeze(self):
        self.freeze=False
        print("your account is unfrozen")   
    
    def get_transanction_history(self):
        for i in self.get_transanction_history:
            print(f"{1['type']}:{i['amount']}")

    def transfer_funds(self,transfer_amount,beneficiary_account):
        if transfer_amount>self.__balance:
            print(f"you transfered {transfer_amount}to {beneficiary_account}")
        else:
            print("you have insufficient funds")
    
    def close_account(self):
        if self.status=='active':
          self.status=='closed'
          print("account is closed")
        else:
            print("already closed")