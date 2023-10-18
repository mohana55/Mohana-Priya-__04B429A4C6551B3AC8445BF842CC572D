
class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}"

# Creating an instance of the BankAccount class
account1 = BankAccount("12345", "John Doe")

# Testing deposit and withdrawal
account1.deposit(1000)
account1.withdraw(200)
account1.withdraw(1500)  # This should display an error message

# Displaying the account balance
print(account1.display_balance())
      