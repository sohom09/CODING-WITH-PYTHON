#Python program to calculate monthly EMI
p = float(input("Enter the amount: "))
print("EMI Table")
print("EMI Frequency\tInterest Rate")
print("3\t\t10%\n6\t\t12%\n9\t\t14%\n12\t\t15%")
f = float(input("Enter the EMI frequency (3/6/9/12): "))
if f==3:
    t=p+(p*0.1*0.25)
    print("EMI=",t/3)
elif f==6:
    t=p+(p*0.12*0.5)
    print("EMI=",t/6)
elif f==9:
    t=p+(p*0.14*0.75)
    print("EMI=",t/9)
elif f==12:
    t=p+(p*0.15*1)
    print("EMI=",t/12)
else:
    print("Enter a valid frequency")


