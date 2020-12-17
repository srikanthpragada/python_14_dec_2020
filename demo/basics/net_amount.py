# Calculate net amount after discount and tax

price = int(input("Enter price :"))
qty = int(input("Enter Qty :"))

amount = price * qty

if qty > 3:
    discount = amount * 0.30
elif qty > 1:
    discount = amount * 0.20
else:
    discount = 0

after_discount = amount - discount
tax = after_discount * 0.12
net_amount = after_discount + tax

print(f"Amount       : {amount:8.2f}")
print(f"- Discount   : {discount:8.2f}")
print(f"               ----------")
print(f"               {after_discount:8.2f}")
print(f"+ Tax        : {tax:8.2f}")
print(f"               ----------")
print(f"Net Amount   : {net_amount:8.2f}")




