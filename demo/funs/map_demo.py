def next_even(n: int) -> int:
    if n % 2 == 0:
        return n + 2
    else:
        return n + 1


lst = [10, -5, 30, -22, 50]
names = ["Larry", "richards", "Don", "Jack", "bilL"]

# for n in map(abs, lst):
#     print(n)
#
# for n in map(next_even, lst):
#     print(n)


marks = ['70', '46', '94', '77']
print(sum(map(int, marks)))
