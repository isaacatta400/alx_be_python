# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance"""
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available"""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance"""
        print(f"Current Balance: ${self.__account_balance}")

# programming_paradigm/main-0.py

import sys
from bank_account import BankAccount

def main():
    # Create an account with an initial balance of 100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
