def factors(*numbers):
    min_value = min(numbers)
    for v in range(2, min_value // 2 + 1):
        for n in numbers:
            if n % v != 0:
                break
        else:
            print(v)


factors(10, 20, 30)
factors(24, 48, 180)
