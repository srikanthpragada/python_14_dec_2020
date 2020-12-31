def ispositive(n: any) -> bool:
    return n > 0


def hasupper(s: str) -> bool:
    for ch in s:
        if ch.isupper():
            return True

    return False


lst = [10, -5, 30, -22, 50]
names = ["Larry", "richards", "Don", "Jack", "bilL"]

for n in filter(ispositive, lst):
    print(n)


for n in filter(hasupper, names):
    print(n)