class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


account1 = BankAccount("12345", 1000.00)
account1.display_account()

account1.deposit(500.00)
account1.withdraw(200.00)
account1.withdraw(1500.00)  # Insufficient funds
account1.deposit(-100) #negative deposit.
account1.withdraw(-100) #negative withdraw.

account1.display_account()

account2 = BankAccount("67890") #create account with 0 balance
account2.display_account()
