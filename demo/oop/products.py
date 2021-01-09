# Superclass
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.qoh = 0

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty

    def netprice(self):
        return self.price

    def __str__(self):
        return f"{self.name} - {self.price} - {self.qoh}"


# Subclass
class DiscountProduct(Product):
    def __init__(self, name, price, disrate):
        super().__init__(name, price)
        self.disrate = disrate

    def __str__(self):
        return super().__str__() + f" - {self.disrate}"

    # Overriding
    def netprice(self):
        discount = self.price * self.disrate / 100
        return self.price - discount


p = Product("Product1", 10000)
print(p, p.netprice())
dp = DiscountProduct("Product2", 20000, 20)
dp.purchase(10)
print(dp)
print(dp.netprice())
