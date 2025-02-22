#Program to calculate tax - GST
print("GST Table")
print("No.\tCategory\tGST Rate")
print("1\tMedicine\t18%")
print("1\tElectronic\t18%")
print("1\tJwellery\t18%")
print("1\tClothing\t18%")
print("1\tEntertainment\t18%")
print("2\tGrossary\t9%")
print("2\tFood\t\t9%")
print("2\tEducation\t9%")

n=int(input("Enter the item no:"))
item=input("Enter the item category:")
p=float(input("Enter the purchase amount: "))

if n==1:
    gst=p*0.18
elif n==2:
    gst=p*0.09
else:
    print("Enter a valid category no")

print("Item category:",item)
print("Purchase amount:",p)
print("GST:",gst)
print("Total bill amount:",(p+gst))

