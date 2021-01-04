# Number related functions

def ispositive(n):
    """
    Returns true if given number is positive, otherwise false
    """
    return n > 0


def iseven(n):
    return n % 2 == 0


def isprime(n):
    """
        Returns true if given number is prime, otherwise false
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


print(f'Name : {__name__}')
if __name__ == '__main__':
    print('Executing module!')
else:
    print('Importing module!')
