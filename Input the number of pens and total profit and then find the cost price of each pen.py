#to find cost price of each pen
A = float(input("Enter the total selling price:"))
x = int(input("Enter the number of pens:"))
SP = A/x
I = float(input("Enter the Given Percentage:"))
print("The selling price of each pen is=",SP)
F = input("Gain or Loss:")
if F == "Gain":
    print("The total cost price of the pens = ",(100*SP)/(100+I))
elif F == "Loss":
    print("The total cost price of the pens = ",(100*SP)/(100-I))
else:
    print("U comitted Tax Fraud")
