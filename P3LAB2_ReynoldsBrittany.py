#Print menu
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")

#Declare options as a dictionary
d_1={"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}

#Prompt for input 
print("\nSelect first service:\n",end="")
s1=input()
print("Select second service:\n",end="")
s_2=input()

#Compare and print result 
print("\nDavy's auto shop invoice\n")
if s1!='-' and s_2!='-':
 print("Service 1: "+s1+", $"+ str(d_1[s1]))
 print("Service 2: "+s_2+", $"+ str(d_1[s_2]))
 result=d_1[s1]+d_1[s_2]
elif s1=='-':
 print("Service 1: "+"No service")
 print("Service 2: "+s_2+", $"+ str(d_1[s_2]))
 result=d_1[s_2]
else:
 print("Service 1: "+s1+", $"+ str(d_1[s1]))
 print("Service 2: "+"No service")
 result=d_1[s1]

print("\nTotal: $"+str(result))