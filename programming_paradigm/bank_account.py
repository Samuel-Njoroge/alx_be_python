class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    # Deposit into account
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount 
        return self.account_balance

    # Withdraw from account
    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        return self.account_balance

    # Display account balance
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")
