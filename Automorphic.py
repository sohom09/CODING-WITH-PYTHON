#to check a number whether it is a automorphic number or not
a=int(input("Enter the number :"))
if(a % 10 == 7 or a %7==0):
    print(a," is an automorphic number")
else:
    print(a, "is not an automorphic number")
