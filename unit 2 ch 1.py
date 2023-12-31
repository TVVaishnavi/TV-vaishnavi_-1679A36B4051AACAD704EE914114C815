class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance

  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited ₹{}, New balance is ₹ {}".format(amount, self.__account_balance))

    else:
      print("Invalid deposit amount")
      
  def withdraw(self, amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print("withdraw ₹{}, New balance: ₹{}".format(amount,self.__account_balance))
      
    else:
      print("Invaild withdrawal amount")
      

  def display_balance(self):
    print("Account balance for {}(Account #{}):₹{}".format(self.__account_holder_name,self.__account_number, self.__account_balance))
    

account=BankAccount(account_number="1234578979",
                    account_holder_name="demon",
                   initial_balance=1000.0)

                    
account.deposit(1000.0)
      