#Input three sides and print the area of a Scelene triangle.
a=float(input("enter the first side of the traingle="))
b=float(input("enter the second side of the traingle="))
c=float(input("enter the third side of the traingle="))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of the scalene traingle=",area)
