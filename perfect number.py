s=0
n=int(input("Enter a number: "))
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("This is a perfect number")
else:
    print("This is not a perfect number")
