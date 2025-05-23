
##############################################
# YZV 102E/104E 23-24 Spring Term Midterm 2 Q1
##############################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS
###################################
class Account:
   def __init__(self, account_number, balance, account_holder_name):
       self.account_number = account_number
       self.balance = balance
       self.account_holder_name = account_holder_name


   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           print(f"Deposited ${'{:.2f}'.format(amount)} into account {self.account_number}.")
       else:
           print("Invalid deposit amount.")


   def withdraw(self, amount):
       if amount > 0:
           if self.balance >= amount:
               self.balance -= amount
               print(f"Withdrew ${'{:.2f}'.format(amount)} from account {self.account_number}.")
           else:
               print("Insufficient funds.")
       else:
           print("Invalid withdrawal amount.")


   def __str__(self):
       return (f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}"
               f"\nBalance: ${'{:.2f}'.format(self.balance)}")

             
class SavingsAccount(Account):
   def __init__(self, account_number, balance, account_holder_name, interest_rate):
       super().__init__(account_number, balance, account_holder_name)
       self.interest_rate = interest_rate


   def calculate_interest(self):
       interest_amount = (self.balance * self.interest_rate) / 100
       self.balance += interest_amount
       print(f"Interest of ${'{:.2f}'.format(interest_amount)} added to account {self.account_number}.")


   def __str__(self):
       return super().__str__() + f"\nInterest Rate: {self.interest_rate}%"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   while True:
       account_number = input()
       if account_number == "exit":
           break
       else:
           balance = float(input())
           account_holder_name = input()
           interest_rate = float(input())
           withdraw_amount = float(input())
           deposit_amount = float(input())
           account = SavingsAccount(account_number, balance, account_holder_name, interest_rate)
           print(account)
           account.withdraw(withdraw_amount)
           print(f"After withdraw: {'{:.2f}'.format(account.balance)}")
           account.deposit(deposit_amount)
           print(f"After deposit: {'{:.2f}'.format(account.balance)}")
           account.calculate_interest()
           print(f"After interest rate: {'{:.2f}'.format(account.balance)}")



##############################
# DO NOT CHANGE BELOW
##############################

if __name__ == '__main__':
    while True:
        account_number = input()
        if account_number == "exit":
            break
        else:
            balance = float(input())
            account_holder_name = input()
            interest_rate = float(input())
            withdraw_amount = float(input())
            deposit_amount = float(input())
            account = SavingsAccount(account_number, balance, account_holder_name, interest_rate)
            print(account)
            account.withdraw(withdraw_amount)
            print(f"After withdraw: {'{:.2f}'.format(account.balance)}")
            account.deposit(deposit_amount)
            print(f"After deposit: {'{:.2f}'.format(account.balance)}")
            account.calculate_interest()
            print(f"After interest rate: {'{:.2f}'.format(account.balance)}")
