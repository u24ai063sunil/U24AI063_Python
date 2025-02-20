class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}  # Dictionary to store accounts (account_number: account_details)

    def create_account(self, account_number, customer_name, initial_balance=0):
        if account_number in self.accounts:
            print(f"Account number {account_number} already exists.")
            return False

        self.accounts[account_number] = {
            "customer_name": customer_name,
            "balance": initial_balance,
            "transactions": []  # List to store transaction history
        }
        print(f"Account {account_number} created successfully for {customer_name}.")
        return True

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Account number {account_number} not found.")
            return False

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self.accounts[account_number]["balance"] += amount
        self.accounts[account_number]["transactions"].append(f"Deposit: +{amount}")
        print(f"Deposited {amount} into account {account_number}.")
        return True

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Account number {account_number} not found.")
            return False

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if self.accounts[account_number]["balance"] < amount:
            print("Insufficient funds.")
            return False

        self.accounts[account_number]["balance"] -= amount
        self.accounts[account_number]["transactions"].append(f"Withdrawal: -{amount}")
        print(f"Withdrawn {amount} from account {account_number}.")
        return True

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            print(f"Account number {account_number} not found.")
            return None

        return self.accounts[account_number]["balance"]

    def get_transaction_history(self, account_number):
      if account_number not in self.accounts:
            print(f"Account number {account_number} not found.")
            return None

      return self.accounts[account_number]["transactions"]

    def display_account_details(self, account_number):
        if account_number not in self.accounts:
            print(f"Account number {account_number} not found.")
            return

        account = self.accounts[account_number]
        print(f"Account Number: {account_number}")
        print(f"Customer Name: {account['customer_name']}")
        print(f"Balance: {account['balance']}")
        print("Transaction History:")
        for transaction in account["transactions"]:
            print(f"  {transaction}")
        print("-" * 20)


my_bank = Bank("SBI")

my_bank.create_account(394327, "Sunil", 1000)
my_bank.create_account(543218, "Vikram")
my_bank.deposit(394327, 500)
my_bank.withdraw(394327, 200)
my_bank.deposit(543218, 100)
my_bank.withdraw(543218, 50)

my_bank.display_account_details(394327)
my_bank.display_account_details(543218)

print(f"Sunil's balance: {my_bank.get_balance(394327)}")
print(f"Vikram's transaction history: {my_bank.get_transaction_history(543218)}")

my_bank.create_account(394327, "Charlie") #attempt to create duplicate account.
my_bank.withdraw(99999, 100) #attempt to withdraw from nonexistant account.
