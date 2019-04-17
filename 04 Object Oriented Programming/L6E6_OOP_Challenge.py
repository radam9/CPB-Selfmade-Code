#OOP Challenge
class BAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f'Transaction Complete!\nYour new balance is ${self.balance}')
    def withdraw(self,amount):
        if amount > self.balance:
            return "Transaction denied, you don't have enough balance"
        else:
            self.balance -= amount
            print(f'Transaction Complete!\nYour new balance is ${self.balance}')
    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'

a1 = BAccount('Jose',100)
print(a1)
a1.owner
a1.balance
a1.deposit(50)
a1.balance
a1.withdraw(75)
a1.withdraw(1)
