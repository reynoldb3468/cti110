
# Reading input prices from the user
current_price = int(input())
last_months_price = int(input())

# Calculating estimated monthly mortagage
est_mort = current_price*0.051/12

# Printing output
print("This house is ${}. The change is ${} since last month.".format(current_price,current_price-last_months_price))
print("The estimated monthly mortgage is ${:.2f}.".format(est_mort))
   