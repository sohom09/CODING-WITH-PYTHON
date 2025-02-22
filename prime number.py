c=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
        break
if(c==2):
    print("The number is a prime number")
else:
    print("This number is not a prime number")
