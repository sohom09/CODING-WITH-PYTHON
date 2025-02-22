##To calculate perimeter/circumference and area of few mathematical shapes
import math
#calculating the area and perimeter of a triangle
a=float(input("Enter the first side of the triangle : "))
b=float(input("Enter the second side of the triangle : "))
c=float(input("Enter the third side of the triangle : "))
s=(a+b+c)/2 #Calculating the Semi-Perimeter of the triangle
area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Calculating the Area of the triangle
print("Perimeter of the triangle : " , s*2)
print("Area of the triangle : " , area)

#calculating the area and perimeter of a rectangle
l=float(input("Enter the length of the rectangle :"))
b=float(input("Enter the breadth of the rectangle :"))
p=2*(l+b) #calculating the perimeter of the rectangle
area=l*b #calculating the area of the rectangle
print("Perimeter of the rectangle : " , p)
print("Area of the rectangle : " , area)

#calculating the area and perimeter of a square
n=float(input("Enter the side of the square : "))
p=4*n #calculating the perimeter
area=n*n #calculating the area
print("Perimeter of the square : " , p)
print("Area of the square : " , area)

#calculating the area and circumference of a circle
r=float(input("Enter the radius of the circle :"))
circum=2*(math.pi)*r #calculating the circumference
area=math.pi*r*r #calculating the area
print("circumference of the circle : " , circum)
print("Area of the circle : " , area)
