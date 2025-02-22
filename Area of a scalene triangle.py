#Program to print the Area of a Scalene Triangle
#Taking the Sides of the Triangle as input from the User
import math
a = float(input('Enter the first side of the Triangle='))
b = float(input('Enter the second side of the Triangle='))
c = float(input('Enter the third side of the Triangle='))
#Calculating the Semi-Perimeter of the Triangle
s = (a+b+c)/2
#Calculating the Area of the Triangle
ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
#Printing the Area of the Triangle
print ("The area of the Scalene Triangle is = ",ar)

