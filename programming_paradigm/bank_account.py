class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    # Deposit into account
    def deposit(self, account_balance, amount):
        return account_balance + amount 

    # Withdraw from account
    def withdraw(self, account_balance, amount):
        return account_balance - amount

    # Display account balance
    def display_balance(self, account_balance):
        return account_balance
