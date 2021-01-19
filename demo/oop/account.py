class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        # return f"Insufficient balance : {self.balance} for withdraw amount {self.amount}"
        return f"You wanted to withdraw {self.amount}, but only {self.balance} is available for withdraw!"


class SavingsAccount:
    minbal = 10000
    intrate = 2.5

    def __init__(self, acno, ahname):
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal < amount:
            raise InsufficientFundsError(self.balance - SavingsAccount.minbal, amount)

        self.balance -= amount

    def getbalance(self):
        return self.balance


s = SavingsAccount(1, "James")
s.email = "abc@gmail.com"
s.deposit(10000)
try:
    s.withdraw(15000)
except InsufficientFundsError as ex:
    print(ex)

print(s.getbalance())
