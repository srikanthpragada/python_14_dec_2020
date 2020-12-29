# Keyword-only arguments
def interest(*, rate, amount, period):
    return (amount * rate / 100) * period / 365


# i = interest(10000, 10, 300)
i = interest(period=200, rate=20, amount=10000)
print(i)
