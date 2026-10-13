class BankAccount:
  def __init__(self, account_number, balance):
    self.__account_number = int(account_number)
    self.__balance = float(balance)

  #setter and getter methods for account_number
  def set_account_number(self, account_number):
    self.__account_number = account_number

  def get_account_number(self):
    return self.__account_number

  #setter and getter methods for balance
  def set_balance(self, balance):
    if balance > 0:
      self.__balance = balance
    else:
      print("The balance must not be a negative number.")
      
  def get_balance(self):
    return self.__balance

@property
def account_number(self):
  return self.__account_number

@property
def balance(self):
  return self.__balance

a1 = BankAccount(12345, 1000)

#use the setter methods
account.set_account_number("9876543210")
account.set_balance("7500")
account.set_balance("-1000")

#use the getter methods
print("Account Number:", account.account_number
print("Balance: {:,.2f}".format(account.balance))
