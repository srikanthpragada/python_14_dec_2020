def get_code(st):
    return st[2:]


lst = [10, -5, 30, -22, 50]
names = ["Larry", "Richards", "Don", "Jack", "Xi"]
codes = ['AB3455', 'XY4822', 'PQ1234', 'AB1876']

# for n in sorted(lst, key = abs):
#     print(n)

#
# for n in sorted(names, key = len):
#     print(n)

for v in sorted(codes, key=get_code):
    print(v)
