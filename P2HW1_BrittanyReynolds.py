# Total Purchases
# 2/23/22
# CTI-110 P2HW1 - Total Purchases
# Brittany Reynolds
#

item1 = float(input("Enter the price of item #1"))
item2 = float(input("Enter the price of item #2"))
item3 = float(input("Enter the price of item #3"))
item4 = float(input("Enter the price of item #4"))
item5 = float(input("Enter the price of item #5"))
subtotal = (item1 + item2 + item3 + item4 + item5)
sales_tax = ((item1 + item2 + item3 + item4 + item5) * .07)

print("Enter the price of item #1: ",item1)
print("Enter the price of item #2: ",item2)
print("Enter the price of item #3: ",item3)
print("Enter the price of item #4: ",item4)
print("Enter the price of item #5: ",item5)

print()
print("-------Results-------")
print("Subtotal: ",subtotal)
print("Sales Tax: ",sales_tax)
print("Total: ", subtotal + sales_tax)
