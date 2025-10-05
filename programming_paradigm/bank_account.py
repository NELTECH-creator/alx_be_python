class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if funds are sufficient"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self.account_balance}")
