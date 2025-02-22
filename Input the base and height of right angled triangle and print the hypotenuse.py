# Input the base and height of right angled triangle and print the hypotenuse.
from math import sqrt
base=float(input("Enter the base of right angled traingle= "))
height=float(input("Enter the height of right angled traingle= "))
hypotenuse=sqrt(base**2+height**2)
print("The length of the hypotenuse is: ",hypotenuse)
