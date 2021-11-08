#Parent Class: User
#Holds details about a user
#Has a function to show user details

#Child Class: Bank
#Inherits all the attributes and methods from parent class 'User'
#Stores details about the account balance
#Allows deposits, withdraw, view_balance

class Account:
    def __init__(self, name, age, account_type):
        self.name = name
        self.age = age
        self.account_type = account_type

    def show(self):
        print(f'User Name: {self.name}\nUser Age: {self.age}\nAccount Type: {self.account_type}')


class Bank(Account):
    def __init__(self, name, age, account_type):
        super().__init__(name, age, account_type)
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Your account balance is now: £{self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("No can do")
        self.account_balance -= amount

    def view_balance(self):
        print(f'Your account balance is {self.account_balance}')