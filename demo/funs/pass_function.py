def detect_type(num, task):
    return task(num)  # Call function pointed by task


def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0


print(detect_type(10, iseven))

print(detect_type(-10, ispositive))

