# positional-only arguments - 3.8
def interest(amount: float, rate: float, /, days: int = 365) -> float:
    return (amount * rate / 100) * days / 365


i = interest(10000, 10, 300)
i = interest(10000, 15, days=200.5)
# i = interest(period=200, rate=20, amount=10000)
print(i)
