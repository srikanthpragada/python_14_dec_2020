
def isprime(n):
    for v in range(2, n//2 + 1):
        if n % v == 0:
            return False

    return True


print(isprime(11), isprime(35), isprime(3939391113))
