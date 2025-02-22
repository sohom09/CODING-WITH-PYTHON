#python program to calculate the tax and accept the monthly salary
s=float(input("Enter salary of a person="))
if s<=50000:
    t=s*0.05
elif s>50000 and s<=60000:
    t=s*0.07
elif s>60000 and s<=70000:
    t=s*0.08
else:
    t=s*0.10
print("Salary=",s,"\tTax=",t)
