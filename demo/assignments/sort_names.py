# Sort names by ignoring leading and trailing spaces and case
def trim(n):
    return n.strip().lower()


names = ['   Larry Ellison  ', ' Larry Page', '   Elon Musk    ',
         'bill Gates', 'Sergy Brin', '   micheal dell  ']

for n in sorted(names, key=trim):
    print(n)
