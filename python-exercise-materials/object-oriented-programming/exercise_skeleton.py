"""
EXERCISE SKELETON - Object Oriented Programming in Python
=============================================================
Fill in the TODO sections below. Run the file and check your
output against the example at the bottom.
"""

# =================================================================
# EXERCISE: Bank Account
# =================================================================
# Create a BankAccount class that represents a bank account.
#
# The class should have:
#   - owner_name attribute
#   - balance attribute
#
# And provide methods:
#   - deposit(amount)  -> adds the given amount to the balance
#   - withdraw(amount) -> subtracts the given amount if the balance
#                          is sufficient; otherwise, print
#                          "Insufficient balance."
#
# Create at least two BankAccount objects and test both methods.
#
# Example:
#   Account: John
#   Initial balance: 1,000,000
#   Deposit: 500,000
#   Withdraw: 300,000
#   Final balance: 1,200,000
#
# HINT: use __init__(self, owner_name, balance) to set up each
#       object's own owner_name and balance when it's created.
class BankAccount:
    def __init__(self, owner_name, balance):
        # TODO: store owner_name and balance on self
        pass

    def deposit(self, amount):
        # TODO: add amount to self.balance
        pass

    def withdraw(self, amount):
        # TODO: if self.balance >= amount, subtract amount
        # TODO: otherwise, print "Insufficient balance."
        pass


# =================================================================
# Test your BankAccount class
# =================================================================
# NOTE: this will raise an AttributeError until you fill in the
# TODOs above (owner_name/balance are never set on self) - that's
# expected, keep going until it passes.
if __name__ == "__main__":
    john_account = BankAccount("John", 1_000_000)
    john_account.deposit(500_000)
    john_account.withdraw(300_000)
    print(f"Account: {john_account.owner_name}")
    print(f"Final balance: {john_account.balance}")   # 1,200,000

    print("-" * 40)

    emily_account = BankAccount("Emily", 200_000)
    emily_account.deposit(100_000)
    emily_account.withdraw(500_000)   # should print "Insufficient balance."
    print(f"Account: {emily_account.owner_name}")
    print(f"Final balance: {emily_account.balance}")   # 300,000 (withdraw failed)
