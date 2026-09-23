class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("current balance:", self.balance)

# Creating an account
account = BankAccount(1000)

account.display_balance()  

account.deposit(500)
account.display_balance()

account.withdraw(300)
account.display_balance()

account.withdraw(1500)  
