#Input a number and print whether it is a prime or composite number
n=int(input("Enter a positive number (except 0) for checking prime or composite="))
count=0
for i in range(2,n):
    if(n%i==0):
        count=1
        break
if(count==0):
    print(n," is a prime number")
else:
    print(n," is a composite number")


