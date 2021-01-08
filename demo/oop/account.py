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
            raise ValueError("Insufficient Funds")

        self.balance -= amount

    def getbalance(self):
        return self.balance


s = SavingsAccount(1, "James")
s.email = "abc@gmail.com"
s.deposit(10000)
s.withdraw(15000)
print(s.getbalance())
