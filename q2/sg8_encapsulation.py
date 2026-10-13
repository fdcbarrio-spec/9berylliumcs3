#create BankAccount class
class BankAccount:
  
    #initialize private attributes 
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    #setter method for account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    #setter method for balance 
    def set_balance(self, balance):
        #check if balance isn't negative
        if balance >= 0:
            self.__balance = balance
        else:
            #display a warning if balance is negative
            print("The balance must not be a negative number.")

    #getter method for account number
    @property
    def account_number(self):
        return self.__account_number

    #getter method for balance
    @property
    def balance(self):
        return self.__balance

#create an object of the bank account class
a1 = BankAccount(12345, 1000)

#display account information 
print("Account 1")
print("Account Number:", a1.account_number)
print("Balance: {:.2f}".format(a1.balance))

#update balance to -100
print("\nUpdate balance to -100")
a1.set_balance(-100)

#display bank account's new information after the update
print("Account Number:", a1.account_number)
print("Balance: {:.2f}".format(a1.balance))
